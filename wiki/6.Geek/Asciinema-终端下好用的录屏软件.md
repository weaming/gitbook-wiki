### Official website

[asciinema - Record and share your terminal sessions, the right way](https://asciinema.org/)

>具体原理简单点说，就是把终端显示和时间戳记录成 json 形式，然后使用 javascript 脚本解析出来。配合官方提供的 CSS 样式，乍看起来以为是视频播放器，然而它却是不折不扣的文本。
相比视频录屏或 GIF 动图的方式，文件体积小的不可思议（比如以下时长2:49的录屏仅为325KB），不需缓冲即可播放，可以更方便的分享给他人或者嵌入到网页中。

### 官方介绍

- Simple recording: Record right where you work - in a terminal. To start just run asciinema rec, to finish hit Ctrl-D or type exit.
- Copy & paste: Any time you see a command you'd like to try in your own terminal just pause the player and copy-paste the content you want. It's just a text after all!
- Embedding: Easily embed an asciicast player in your blog post, project documentation page or in your conference talk slides.

### 如何食用

- Install: `sudo apt-get install asciinema`
- Start: `asciinema [rec]`
- Finish: `Ctrl`+`d` or `exit`

在打开的链接中，点击分享，即可出现图片、Markdow、嵌入网页三种分享方式。

官方嵌入网页说明：[Sharing & embedding - asciinema](https://asciinema.org/docs/embedding)

```text
$ asciinema --help
usage: asciinema [-h] [-y] [-c <command>] [-t <title>] [action]

Asciicast recorder+uploader.

Actions:
 rec              record asciicast (this is the default when no action given)
 auth             authenticate and/or claim recorded asciicasts

Optional arguments:
 -c command       run specified command instead of shell ($SHELL)
 -t title         specify title of recorded asciicast
 -y               don't prompt for confirmation
 -h, --help       show this help message and exit
 -v, --version    show version information
```

### 本地保留数据

 Another improvement to asciinema rec is its ability to save the recording to a local file.

	asciinema rec demo.json

This saves the session to demo.json file. Now, you can replay it directly in your terminal:

	asciinema play demo.json

Finally, if you’re happy about it and you want to share it on asciinema.org just run:

	asciinema upload demo.json

If you don’t need to keep your recording local and just want to record and upload in one step, you can still `asciinema rec` without a filename.

### Example

<script type="text/javascript" src="https://asciinema.org/a/dlrhoklhmo0fgvs9u5fbzbcx5.js" id="asciicast-dlrhoklhmo0fgvs9u5fbzbcx5" async></script>


### Links

- [1.0 · asciinema blog](http://blog.asciinema.org/post/one-point-o/)