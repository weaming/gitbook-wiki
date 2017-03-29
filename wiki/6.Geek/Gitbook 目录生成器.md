运行生成就好，前提是对`md`文件做好命名。在文件夹之间移动方便多了 :)

Code: (其中`filetree`是我编写的一个库，`pip install -U filetree`安装就成)

最新代码： [gitbook-wiki/gen_summary.py](https://github.com/weaming/gitbook-wiki/blob/master/gen_summary.py)

```Python
# coding: utf-8

import sys
from filetree import File


def link(text, url, prefix='', suffix=''):
    if text.endswith('.md'):
        text = text.replace('.md', '')
    return '{}[{}]({}){}'.format(prefix, text, url, suffix)


def main():
    lines = []
    deepth = 0
    prefix = '* '

    for dir in sorted(F.dirs, key=lambda x: int(x.basename.split('.')[0])):
        if 'index.md' in F:
            lines.append(link(dir.basename, './' + dir.n_relative_paths(2), prefix=prefix))
        else:
            lines.append(prefix + dir.basename.upper())
        for md in reversed(sorted(list(dir), key=lambda x: x.mtime)):
            if not md.path.endswith('.md'):
                continue
            deepth += 1
            lines.append(link(md.basename, './' + md.n_relative_paths(3), prefix='    '*deepth+prefix))
            deepth -= 1

    for md in F.files:
        if not md.path.endswith('.md'):
            continue
        lines.append(link(md.basename, './' + md.n_relative_paths(2), prefix='    '*deepth+prefix))

    with open('summary.md', 'w') as out:
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
```
