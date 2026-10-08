#!/usr/bin/env python3
"""Deterministic pipeline.md counter and ships-log line builder.

Usage:
    python3 count-pipeline.py [PIPELINE_MD] ["what changed"] [--log PIPELINE_LOG_MD]

PIPELINE_MD defaults to $JOB_SEARCH_DIR/pipeline.md, or
~/Documents/job-search/pipeline.md when JOB_SEARCH_DIR is not set.
With --log, the line is also appended to that file (created if missing).
Timestamps use the local time zone, or $TZ if set.

Use this rather than counting by hand: hand counts drift when an entry is
missing its `Stage:` field, or when entries are deduplicated by company name.
"""
import argparse
import datetime
import io
import os
import re
import sys
from collections import Counter

DEFAULT_DIR = os.path.expanduser(os.environ.get('JOB_SEARCH_DIR', '~/Documents/job-search'))


def counts(path):
    s = io.open(path, encoding='utf-8').read()
    ai = s.find('## ACTIVE')
    if ai == -1:
        sys.exit('No "## ACTIVE" section found in %s' % path)
    ci = s.find('\n## CLOSED', ai)
    act_end = ci if ci != -1 else s.find('\n## ', ai + 1)
    act = s[ai:act_end if act_end != -1 else len(s)]
    if ci != -1:
        end = s.find('\n## ', ci + 1)
        clo = s[ci:end if end != -1 else len(s)]
    else:
        clo = ''
    rows = []
    for e in re.split(r'\n(?=### )', act)[1:]:
        name = e.split('\n', 1)[0][4:].strip()
        m = re.search(r'\*\*Stage:\*\*\s*([A-Z]+)', e)
        k = re.search(r'\*\*Kind:\*\*\s*(\S+)', e)
        rows.append((m.group(1) if m else '?', k.group(1) if k else None, name))
    c = Counter(st for st, _, _ in rows)
    app = [kd for st, kd, _ in rows if st == 'APPLIED']
    warm = sum(1 for kd in app if kd and '\U0001f91d' in kd)   # 🤝 warm
    real = sum(1 for kd in app if kd and '⭐' in kd)       # ⭐ real pursuit
    cold = len(app) - warm - real                               # missing Kind = cold
    unknown = [n for st, _, n in rows if st == '?']
    mid = c.get('OFFER', 0) + c.get('LOOP', 0) + c.get('SCREEN', 0)
    return dict(bytes=len(s.encode('utf-8')), active=len(rows),
                closed=len(re.findall(r'(?m)^### ', clo)),
                offer=c.get('OFFER', 0), loop=c.get('LOOP', 0),
                screen=c.get('SCREEN', 0), applied=len(app), warm=warm,
                real=real, cold=cold, sourced=c.get('SOURCED', 0), mid=mid,
                unknown=unknown)


def line(d, note=''):
    ts = datetime.datetime.now().astimezone().strftime('%Y-%m-%d %H:%M %Z')
    warn = ''
    if d['unknown']:
        warn = ' ⚠ NO-STAGE: ' + '; '.join(n[:40] for n in d['unknown'])
    return ('- `%s` · %db · A%d C%d · **MID %d** (O%d L%d S%d) · '
            'APP %d (%d\U0001f91d/%d⭐/%d\U0001f4cb) · SRC %d — %s%s'
            % (ts, d['bytes'], d['active'], d['closed'], d['mid'], d['offer'],
               d['loop'], d['screen'], d['applied'], d['warm'], d['real'],
               d['cold'], d['sourced'], note or '(no note given)', warn))


def main():
    p = argparse.ArgumentParser(description='Count pipeline.md and build a ships-log line.')
    p.add_argument('pipeline', nargs='?', default=os.path.join(DEFAULT_DIR, 'pipeline.md'))
    p.add_argument('note', nargs='?', default='')
    p.add_argument('--log', help='append the line to this ships-log file')
    a = p.parse_args()
    d = counts(os.path.expanduser(a.pipeline))
    out = line(d, a.note)
    print(out)
    if a.log:
        with io.open(os.path.expanduser(a.log), 'a', encoding='utf-8') as f:
            f.write(out + '\n')
    if d['unknown']:
        sys.stderr.write('WARNING: entries with no Stage field: %r\n' % d['unknown'])


if __name__ == '__main__':
    main()
