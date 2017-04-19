gvim74 提示报错 “无法加载库python27.dll”
--
官方提供的gvim安装文件默认是支持python和python3两种模式的,编译时带有该选项,但并没有附带对应的运行库和运行环境.所以在本地没有安装python时直接在vim中执行

    :py print 'ok'

会提示无法加载python27.dll, 针对于这种情况,请到官方下载 windows 版本的 **32位** 的python 2.7.x 安装文件. 使用64位的python无法正常在gvim中使用.

python3.x系列在某些vim相关插件中仍不支持,所以依旧推荐使用2.7.x

我是64位win7，偶然一天不知道干啥了，一些插件提示说需要python27，我明明装了这个版本，却继续报错。去官网装了32位版本python2.7后，果然不报错了。
