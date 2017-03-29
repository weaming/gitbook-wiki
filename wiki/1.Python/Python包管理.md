distutils、distutils2
--
[distutils](https://docs.python.org/3/library/distutils.html)是 python 标准库的一部分，2000年发布。使用它能够进行 python 模块的 [安装](https://docs.python.org/3/install/index.html) 和 [发布](https://docs.python.org/3/distutils/index.html)。

distutils2 被设计为 distutils 的替代品，后来这个计划停滞了。


setuptools、easy_install、ez_setup.py
--
`setuptools` 是一个为了增强 distutils 而开发的集合，2004年发布。它包含了 easy_install 这个工具。

`ez_setup.py` 是 setuptools 的安装工具。ez 是 easy 的缩写。

使用方式：

- 从 PyPI 上安装一个包：`easy_install requests`
- 从网络文件安装（下载并安装）：`easy_install http://path/to/MyPackage-1.2.3.tgz`
- 从一个本地 .egg 格式文件安装：`easy_install /path/to/MyPackage-1.2.3.egg`

distribute 是 setuptools 的一个分支版本，后来又合并到了setuptools。


pip
--
pip 是目前 python 包管理的事实标准，2008年发布。它被用作 easy_install 的替代品，但是它仍有大量的功能建立在 setuptools 组件之上。

pip 希望不再使用 Eggs 格式（虽然它支持 Eggs），而更希望采用“源码发行版”（使用 python setup.py sdist 创建）。

pip使用方式：

- pip 可以利用 `requirments.txt` 来实现依赖的安装。
- 支持 git/svn/hg 等流行的 VCS 系统，可以直接从 gz 或者 zip 压缩包安装，支持搜索包，以及指定服务器安装等等功能。
- pip 提供了一个 wheel 子命令来安装 wheel 包。需要先安装 wheel 模块。

setup.py vs requirements.txt [¶](http://pyzh.readthedocs.org/en/latest/python-setup-dot-py-vs-requirements-dot-txt.html)
--
- Python库：那些被开发并且为了其他人来使用而发布的东西，你可以在 PyPI 找到很多Python库。为了更好的推广和传播 自己，Python库会包含很多的信息，比如它的名字，版本号，依赖等等。而 `setup.py` 就是用来提供这些信息的。但是，并没有规定你可以从哪里获取这些依赖库。
- Python应用：指你所要部署的一些东西，这是区别于我们之前所讲的Python库的。一个应用经常会有很多依赖，或许会很复杂。这些依赖里很多没有一个名字，或者没有我们说所的那些信息。这便反映了 pip 的requirements文件所做的事情了。每个依赖都标明了准确的版本号，一般一个Python库对依赖的版本比较宽松，而一个应用則会依赖比较具体的版本号。虽然也许跑其他 版本的 requests 并不会出错，但是我们在本地测试顺利后，我们就会希望在线上也跑相同的版本。执行`pip install -r requirements.txt`来安装。

setup.py
```
from setuptools import setup

setup(
    name="MyLibrary",
    version="1.0",
    install_requires=[
        "requests",
        "bcrypt",
    ],
    # ...
)
```

requirements.txt
```
# This is an implicit value, here for clarity
--index https://pypi.python.org/simple/

MyPackage==1.0
requests==1.2.0
bcrypt==1.0.2
```
### 从抽象到具体
上面这个requirements.txt文件的头部有一个 `--index https://pypi.python.org/simple/` ，一般如果你不用声明这项，除非你使用的不是`PyPI`。然而它却是 `requirements.txt` 的一个重要部分， 这一行把一个抽象的依赖声明 `requests==1.2.0` 转变为一个具体的依赖声明 `requests 1.2.0 from pypi.python.org/simple/`

在 `setup.py` 中，也存在一个 `install_requires` 表来指定依赖的安装。这一功能除去了依赖的抽象特性，直接把依赖的获取url标在了setup.py里。[Link](http://pyzh.readthedocs.org/en/latest/python-setup-dot-py-vs-requirements-dot-txt.html)
```
from setuptools import setup

setup(
    # ...
    dependency_links = [
        "http://packages.example.com/snapshots/",
        "http://example2.com/p/bar-1.0.tar.gz",
    ],
)
```

wheel
--
wheel 本质上是一个 zip 包格式，它使用 .whl 扩展名，用于 python 模块的安装，它的出现是为了替代 Eggs。

wheel 还提供了一个 `bdist_wheel` 作为 setuptools 的扩展命令，这个命令可以用来生成 wheel 包。

pip 提供了一个 wheel 子命令来安装 wheel 包。

`setup.cfg` 可以用来定义 wheel 打包时候的相关信息。

[Python Wheels](http://pythonwheels.com/) 网站展示了使用 Wheels 发行的 python 模块在 PyPI 上的占有率。

**.whl文件下载：**http://www.lfd.uci.edu/~gohlke/pythonlibs/

总结
--
安装

- Use pip to install Python packages from PyPI. Depending how pip is installed, you may need to also install wheel to get the benefit of wheel caching.
- Use virtualenv, or pyvenv to isolate application specific dependencies from a shared Python installation.
- If you’re looking for management of fully integrated cross-platform software stacks, consider buildout (primarily focused on the web development community) or Hashdist, or conda (both primarily focused on the scientific community).

打包

- Use `setuptools` to define projects and create Source Distributions.
- Use the `bdist_wheel` setuptools extension available from the wheel project to create wheels. This is especially beneficial, if your project contains binary extensions.
- Use `twine` for uploading distributions to PyPI.

第三方库安装路径
--
Debian系的特殊路径：[Link](http://stackoverflow.com/questions/9387928/whats-the-difference-between-dist-packages-and-site-packages)

>dist-packages instead of site-packages. Third party Python software installed from Debian packages goes into dist-packages, not site-packages. This is to reduce conflict between the system Python, and any from-source Python build you might install manually.

就是说从源代码手动安装，将使用`site-packages`目录。第三方python软件安装到`dist-packages`目录，这是为了减少与操作系统版本的python的冲突，因为Debian系统的许多工具都依赖与系统版本的python。

查找 Python 安装路径
--
```
>>> from distutils.sysconfig import get_python_lib
>>> print(get_python_lib())
```

Links
--
- http://zengrong.net/post/2169.htm
- https://packaging.python.org/en/latest/