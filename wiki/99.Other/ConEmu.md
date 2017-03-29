### 背景

Windows 下想更好的使用 Terminal。[已经决定用 Windows 了……求靠谱好用 Shell - V2EX](https://www.v2ex.com/t/315212)

看到结合多个工具来使用的：

>ConEmu+msys2+pacman+ohmyzsh 的只有我一个？

体验了下ConEmu还不错!除了一些 Vim 里字体乱码问题。

### 如何使用

基本的就不啰嗦了，看他人链接：[工具02：cmd的替代品ConEmu+Clink | LearnIT](https://higoge.github.io/2015/07/22/tools02/)。额外的就补充说明下。

### 配置

![](/img/1610/conemu-setting.jpg)

如果所示，可以配置启动和新建 Tab 时的默认终端，并配置终端启动时的 shell 解释器，如 bash、zsh 等。

### 字体


### 快捷键

| 快捷键         | 操作                              |
| -------------- | --------------------------------- |
| n+w            | 新建一个窗口，输入{cw}或{putty}   |
| win+x          | 新建一个cmd                       |
| win+q          | 标签切换                          |
| win+alt+p      | 开启setting                       |
| win+alt+t      | 配置tasks                         |
| win+数字键     | 切换tabs                          |


#### 题外话

在编辑上面这个快捷键表格的时候发现很痛苦，经过简单搜索，发现了一个方便输入和对齐的VIM插件：

[dhruvasagar/vim-table-mode: VIM Table Mode for instant table creation.](https://github.com/dhruvasagar/vim-table-mode)

`<leader>tm` 开关 table mode。编辑时，输入`|`即可自动对齐，输入`||`即可自动输入一行纵向分割线。