#!/usr/bin/env python
# coding: utf-8

import os
import sys
from filetree import File

__FILE__ = File('.').path

def link(text, url, prefix='', suffix=''):
    if text.endswith('.md'):
        text = text.replace('.md', '')
    return '{}[{}]({}){}'.format(prefix, text, url, suffix)


def main(url_prefix=''):
    lines = []
    deepth = 0
    prefix = '* '

    for dir in sorted(F.dirs, key=lambda x: int(x.basename.split('.')[0])):
        if 'index.md' in dir:
            lines.append(link(dir.basename, '%s/%s/%s' % (path, dir.basename, 'index.md'), prefix=prefix))
        else:
            lines.append(prefix + dir.basename.upper())
        for md in reversed(sorted(list(dir), key=lambda x: x.mtime)):
            if not md.path.endswith('.md'):
                continue
            if md.basename == 'index.md':
                continue
            deepth += 1
            lines.append(link(md.basename, './' + os.path.relpath(md.path, __FILE__), prefix='    '*deepth+prefix))
            deepth -= 1

    for md in F.files:
        if not md.path.endswith('.md'):
            continue
        lines.append(link(md.basename, './' + os.path.relpath(md.path, __FILE__), prefix='    '*deepth+prefix))

    with open('SUMMARY.md', 'w') as out:
        out.write('\n'.join(lines))

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 2:
        path = args[1]
    elif len(args) > 2:
        raise ValueError("Too much command line arguments!")
    else:
        path = './wiki'

    F = File(path)
    main()
