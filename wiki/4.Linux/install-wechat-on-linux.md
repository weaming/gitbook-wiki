## Steps

1. Download tar.gz file on github releases: https://github.com/geeeeeeeeek/electronic-wechat/releases
2. `tar-xvf linux-*.tar.gz`
3. Once it’s extracted,  go to electronic-wechat-linux-x64 or electronic-wechat-linux-ia32 folder
4. then run this command to open Wechat: `./electronic-wechat`

## Make valiable from shell directly

To make our file system clean, we can move the folder to `/usr/local/` directory.

    sudo mv electronic-wechat-linux-x64/ /usr/local/electronic-wechat

or

    sudo mv electronic-wechat-linux-ia32/ /usr/local/electronic-wechat

Then make a symbolic link.

    sudo ln -s /usr/local/electronic-wechat/electronic-wechat /usr/local/bin/wechat

or

    sudo ln -s /usr/local/electronic-wechat/electronic-wechat /usr/local/bin/wechat

So now we just need to press `ALT+F2` and enter wechat command to launch the WeChat client on Linux.

## Links

- [How To Install WeChat on Linux - linuxbabe.com](https://www.linuxbabe.com/desktop-linux/install-wechat-linux)