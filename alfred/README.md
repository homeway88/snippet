# Alfred常用脚本

## 1.ParseIpFromHostName 从主机名称解析IP信息
公司内部的线上机器名称，一般都有固定的模式，里面包含有IP信息，从中提取出IP信息，可以非常方便地登录线上机器 。
主机名称模式，一般是`${应用名}${IP}.${环境}.${地区}`,如`uniface011141031033.online.china`。
其中，IP部分为12位的数字`011141031033`，我们只需要通过正则表达式，就能够提取出其中的IP信息，即`11.141.31.33`。