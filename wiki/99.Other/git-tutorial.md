## 什么是Git

![](/img/git/git.png)

git 是一个**分布式**版本控制软件。与SVN一类的集中式版本控制工具不同，它采用了分布式版本库的作法，不需要服务器端软件，就可以运作版本控制，使得源代码的发布和交流极其方便。


## windows 客户端下载

https://git-scm.com/download/win

以下均在 windows 系统下操作。

## 运行

任意文件夹内右键：
![](/img/git/1.png)

界面：
![](/img/git/2.png)

## 总览

- 本地工作目录（Working Directory）
- 本地版本库/仓库（repository）
 - 工作区有一个隐藏目录`.git`，这个不算工作区，而是Git的版本库。所有的提交历史都储存在这里。
- 远程仓库（比如[Github](https://github.com)）

## 本地基本操作

### 从头开始新建仓库

以下均以命令行形式操作。

    git init <repo-name>

新建空的本地仓库，会新建一个`repo-name`文件夹，里面包含一个 `.git` 的文件夹。

如果不加 `repo-name` ，就会把当前目录作为仓库，直接新建`.git`文件夹。

### 查看状态

    git status

### 查看代码更改状况

    git diff

### 添加跟踪文件

    git add <file-name>

### 提交（commit）

    git commit -m 'commit text'

### 删除提交（reset）
删除最新的两个提交

    git reset --hard HEAD~~

在reset之前的提交可以参照`ORIG_HEAD`。Reset错误的时候，在`ORIG_HEAD`上reset 就可以还原到reset前的状态。

    git reset --hard ORIG_HEAD

### 例子

![](/img/git/3.png)

### 查看历史（log）

![](/img/git/4.png)

## 分支（branch）管理

    git branch <name> # 创建分支
    git branch -b <name> # 创建并切换到新分支
    git branch # 查看所有分支
    git checkout master # 检出master分支
    git branch -v # 查看分支状态
    git branch -d <name> # 删除分支
    git branch -m [<oldbranch>] <newbranch> # 重命名分支

### 合并（merge）

比如要把issue1分支合并到主分支。

    git checkout master
    git merge issue1

### 汇合commit（rebase）

参考：[用rebase -i 汇合提交](http://backlogtool.com/git-guide/cn/stepup/stepup7_5.html)

这样可以使提交看起来更精简。

![](/img/git/rebase1.png)

>它的原理是首先找到这两个分支（即当前分支 experiment、变基操作的目标基底分支 master）的最近共同祖先 C2，然后对比当前分支相对于该祖先的历次提交，提取相应的修改并存为临时文件，然后将当前分支指向目标基底 C3, 最后以此将之前另存为临时文件的修改依序应用。

![](/img/git/rebase2.png)

然后回到 master 分支，进行一次快进合并。

    $ git checkout master
    $ git merge experiment

![](/img/git/rebase3.png)

### 拣选（cherry-pick）

另一种将引入的工作转移到其他分支的方法是拣选。 Git 中的拣选类似于对特定的某次提交的变基。 它会提取该提交的补丁，之后尝试将其重新应用到当前分支上。 这种方式在你只想引入特性分支中的某个提交，或者特性分支中只有一个提交，而你不想运行变基时很有用。 举个例子，假设你的项目提交历史类似：

![](/img/git/cherry-pick1.png)

如果你希望将提交 e43a6 拉取到 master 分支，你可以运行：

    git checkout master
    git cherry-pick e43a6


## Github

### 注册Github

https://github.com/join

### 界面说明

![](/img/git/github.png)

### 生成SSH Key，并添加到Github

参考：https://help.github.com/articles/generating-an-ssh-key/

## 远程仓库交互

克隆（clone），即下载到本地

    git clone URL

URL 有两种形式：https 和 ssh。`https://github.com/id/project.git` 或 `git@github.com:id/project.git`

实际中，末尾的`.git`省略也可正常使用。

SSH 通过证书来验证，HTTPS 通过密码来验证。

其中 https，可以在URL里加入密码，例如 `https://id:password@github.com/id/project.git`，不安全，谨慎使用。

### 提交（push）到远程仓库

    git push

这里会根据上面的 URL 来验证，如果是 ssh ，会通过密钥来验证，如果是 https，会通过密码来验证。

### 更新代码（pull）

    git pull

默认执行“快速合并”。如果这里出现了冲突，必须手动解决冲突。`git status`可以告诉我们冲突的文件。

Git用`<<<<<<<`，`=======`，`>>>>>>>`标记出不同分支的内容，修改后保存。再提交到本地仓库。

    git fetch # 只下载，而不checkout

## 标签（tag）管理
### 本地

首先，切换到需要打标签的分支上。`git branch`查看现有分支，`git checkout master`切换到master分支。

    git tag <name> # 打一个新标签
    git tag # 查看所有标签
    git tag -d <name> # 删除标签
    git show <tagname> # 显示标签详情

标签默认是打在最新提交的commit上的。如果忘了打标签，比如，现在已经是周五了，但应该在周一打的标签没有打，怎么办？

`git log --pretty=oneline --abbrev-commit`查看历史提交，然后：

    git tag <name> f0cc57c

### 远程

命令`git push origin <tagname>`可以推送一个本地标签；

命令`git push origin --tags`可以推送全部未推送过的本地标签；

命令`git push origin :refs/tags/<tagname>`可以删除一个远程标签。

## 配置别名

只需要敲一行命令，告诉Git，以后`st`就表示`status`：

    git config --global alias.st status

其他

    git config --global alias.st status
    git config --global alias.co checkout
    git config --global alias.ci commit
    git config --global alias.br branch
    git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

## 配置Git

Git 提供了一个叫做 git config 的工具（译注：实际是 git-config 命令，只不过可以通过 git 加一个名字来呼叫此命令。），专门用来配置或读取相应的工作环境变量。而正是由这些环境变量，决定了 Git 在各个环节的具体工作方式和行为。这些变量可以存放在以下三个不同的地方：

- `/etc/gitconfig` 文件：系统中对所有用户都普遍适用的配置。若使用 git config 时用 `--system` 选项，读写的就是这个文件。
- `~/.gitconfig` 文件：用户目录下的配置文件只适用于该用户。若使用 git config 时用 `--global` 选项，读写的就是这个文件。
- 当前项目的 Git 目录中的配置文件（也就是工作目录中的 `.git/config` 文件）：这里的配置仅仅针对当前项目有效。每一个级别的配置都会覆盖上层的相同配置，所以 .git/config 里的配置会覆盖 /etc/gitconfig 中的同名变量。

在 Windows 系统上，Git 会找寻用户主目录下的 `.gitconfig` 文件。主目录即 $HOME 变量指定的目录，一般都是 `C:\Documents and Settings\$USER`。此外，Git 还会尝试找寻 `/etc/gitconfig` 文件，只不过看当初 Git 装在什么目录，就以此作为根目录来定位。

参见：[Git - 初次运行 Git 前的配置](https://git-scm.com/book/zh/v1/%E8%B5%B7%E6%AD%A5-%E5%88%9D%E6%AC%A1%E8%BF%90%E8%A1%8C-Git-%E5%89%8D%E7%9A%84%E9%85%8D%E7%BD%AE)

### 账户

    git config --global user.name "weaming"
    git config --global user.email "iweaming@gmail.com"

拓展：https://help.github.com/articles/setting-your-email-in-git/

### 颜色

    git config --global color.status auto
    git config --global color.branch auto
    git config --global color.interactive auto
    git config --global color.diff auto

### push.default

    git config --global push.default current

- nothing - do not push anything.
- matching - push all matching branches. All branches having the same name in both ends are considered to be matching. This is the default.
  - Changed in Git 2.0 from 'matching' to 'simple'
- upstream - push the current branch to its upstream branch.
- tracking - deprecated synonym for upstream.
- current - push the current branch to a branch of the same name.

### core.filemode

If false, the executable bit differences between the index and the working tree are ignored; useful on broken filesystems like FAT.

设置是否检查文件权限，其值默认为'true'，对同样内容、名字的文件，如果其文件权限发生了改变，则会认为发生了'修改'。如果要忽略文件权限的检查，可以将该项的值设置为'false'。

    git config --global core.filemode false

### core.autocrlf

设置Git对行尾的换行符的处理方式。这个设置项主要是为了解决跨平台开发时Windows操作系统与*nix系统上换行符不一致的矛盾。

    git config --global core.autocrlf true

- true：设置为该值时，代码仓库里的代码会保证以*nix的换行符结尾，在用户提交时会把Windows的换行符替换为*nix的换行符，但在用户checkout后将会替换成Windows的换行符。在Windows环境下开发但其合作者中在*nix系统下开发的用户可以将'core.autocrlf'项的值设置为'true'
- input：设置为该值时，代码仓库里的代码和checkout的结果都会保证以*nix的换行符结尾，如果提交时的文件中存在Windows的换行符，Git会将其替换为*nix的换行符。
- false：设置为该值时，Git不对文件行结尾的换行符进行检测和处理。

### `.gitignore`文件

项目中经常会生成一些Git系统不需要追踪(track)的文件。典型的是在编译生成过程中 产生的文件或是编程器生成的临时备份文件。当然，你不追踪(track)这些文件，可以 平时不用`git add`去把它们加到索引中。 但是这样会很快变成一件烦人的事，你发现 项目中到处有未追踪(untracked)的文件; 这样也使`git add .` 和`git commit -a` 变得实际上没有用处，同时`git status`命令的输出也会有它们。

可以在你的顶层工作目录中添加一个叫`.gitignore`的文件，来告诉Git系统要忽略 掉哪些文件，下面是文件内容的示例:

```
# 以'#' 开始的行，被视为注释.
# 忽略掉所有文件名是 foo.txt 的文件.
foo.txt
# 忽略所有生成的 html 文件,
*.html
# foo.html是手工维护的，所以例外.但是如果一个目录被排除了，那么目录中任何文件都永远不可能被重新包含。
!foo.html
#  忽略所有.o 和 .a文件.
*.[oa]
# 忽略test文件夹
test/
# ** 匹配任意路径,
# 忽略任意路径下的foo文件或foo文件夹
**/foo
```

`.gitignore`文件同样可以像其它文件一样加到项目仓库里, 这样项目里的其它开发者也能共享同一套忽略文件规则。

另外，要停止追踪一个文件，可以使用`git rm --cached`。

## 查看帮助（help）

可通过命令来获取帮助

    git --help
    git help branch
    git help -a

## 流程图

![](/img/git/git-arrows.png)

## 参考链接

- [图解Git](https://marklodato.github.io/visual-git-guide/index-zh-cn.html)
- [Git教程](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)
- [猴子都能懂的GIT入门](http://backlogtool.com/git-guide/cn/)
- [自定义Git](http://linusp.github.io/2014/08/02/configure-git.html)
- [gitignore](https://www.kernel.org/pub/software/scm/git/docs/gitignore.html)