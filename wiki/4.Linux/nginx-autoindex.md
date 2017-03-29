开启 autoindex

    autoindex on;

默认为on，显示出文件的确切大小，单位是bytes。
改为off后，显示出文件的大概大小，单位是kB或者MB或者GB

    autoindex_exact_size off;

默认为off，显示的文件时间为GMT时间。
改为on后，显示的文件时间为文件的服务器时间

    autoindex_localtime on;

--------

```
autoindex on;
autoindex_exact_size off;
autoindex_localtime on;
```