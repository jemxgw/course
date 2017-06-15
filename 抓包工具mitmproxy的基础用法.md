# 抓包工具mitmproxy的基础用法

工作中用到的抓包工具常见的windows中的Fiddler，mac中的Charles，今天介绍一款可以在终端中使用的跨平台抓包工具[mitmproxy](http://docs.mitmproxy.org/en/stable/index.html)。

## 1. 安装

mitmproxy的安装非常简单，可以直接通过Homebrew安装。(不知道Homebrew的小伙伴可移步[Homebrew官网](http://brew.sh/index_zh-cn.html)一探究竟)

```bash
$ brew install mitmproxy
```

## 2. 配置

和其他抓包工具一样，就要设置代理，mitmproxy默认的端口是8080，你也可以通过`-p`自定义端口：

```bash
$ mitmproxy -p 8080
```

![](http://o7qrps1cr.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-06-15%20%E4%B8%8B%E5%8D%886.10.10.png)

## 3. 安装证书

 前两部做好后，在终端打开mitmproxy，在浏览器中打开[mitm.it](http://mitm.it/)，下载并根据提示安装相应的证书。

![](http://o7qrps1cr.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-06-15%20%E4%B8%8B%E5%8D%887.22.07.png)

## 4. 常用操作

前三部完成后，我们就可以进行抓包了，输入`?`可以查看帮助文档：

![](http://o7qrps1cr.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-06-15%20%E4%B8%8B%E5%8D%888.03.47.png)

### 4.1 查看抓包结果

比如我们现在打开谷歌，你会看到像下面的抓包结果：

![](http://o7qrps1cr.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-06-15%20%E4%B8%8B%E5%8D%888.13.43.png)

黄色的箭头==>>==指向当前的请求，列表上的请求表明了请求方法、链接、时间、状态码、数据大小。按`ENTER`键即可查看进入查看每个请求的详情：

![](http://o7qrps1cr.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-06-15%20%E4%B8%8B%E5%8D%888.18.45.png)

按`tab`键可以在Request、Response和Detail间切换（也可以通过`H`，`L`左右切换）。

![](http://o7qrps1cr.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-06-15%20%E4%B8%8B%E5%8D%888.27.24.png)

Response中的数据可以以不同的格式展示，按`m`键底部会出现各种数据格式的说明，如果我按`e`，数据即可以Hex格式展示：

![](http://o7qrps1cr.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-06-15%20%E4%B8%8B%E5%8D%888.30.49.png)

按`q`即可回到列表。`q`可以用作回到上一级，也可以退出程序（但是`q`会询问是否退出，`Q`会强制退出。）

### 4.2 修改请求

我们刚才打开google有很多请求，为了新一次的抓包，我希望清楚刚才所有的请求，我们可以按`z`清除列表上的所有抓包请求。

我现在打开 http://httpbin.org/ ，因为我们现在只想观察来自这个网址的请求，不希望别的请求的干扰，这时候我们可以使用过滤请求功能，按`f`键，输入`httpbin\.org`：

只会显示包含httpbin\.org的请求：

![](http://o7qrps1cr.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-06-15%20%E4%B8%8B%E5%8D%888.59.37.png)

我们可以看到，还有两张gif图片，我们同样可以把他们过滤掉：`httpbin\.org & !gif & !facebook`。

我们进入该请求，然后按`e`可以修改该请求，底部提示我们修改相应的参数：

![](http://o7qrps1cr.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-06-15%20%E4%B8%8B%E5%8D%889.03.48.png)

现在我想修改请求的url，我把url改成 http://httpbin.org/ip ，然后按`r`重新发送该请求，我们注意到刚才的页面是一个HTML页面，现在返回的数据是JSON，返回的是我所在的IP。

![](http://o7qrps1cr.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-06-15%20%E4%B8%8B%E5%8D%889.10.12.png)

### 4.3 拦截请求

mitmproxy是一个中间人代理工具，客户端与服务端之间的数据传输都要经过mitmproxy。比如，客户端向服务端发送请求，请求的所有参数都将经过mitmproxy，mitmproxy可以对请求的参数进行修改然后发送给服务端。服务端收到请求后，将响应发送回客户端，又被mitmproxy拦截，mitmproxy可以修改响应内容，然后再发送回客户端。

按`i`，即可进入拦截模式，底部提示我们输入拦截的条件。我们现在在浏览器中打开 http://httpbin.org/ip ，被拦截的请求显示橘黄色，因为浏览器的请求被mitmproxy拦截，所以浏览器一直在等待服务端的响应：

![](http://o7qrps1cr.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-06-15%20%E4%B8%8B%E5%8D%8810.06.16.png)

进入查看该请求，可以按`e`对请求的参数进行修改，现在我不修改请求参数，然后按`a`将请求发送给服务端，服务端的响应被mitmproxy拦截：

![](http://o7qrps1cr.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-06-15%20%E4%B8%8B%E5%8D%8810.12.35.png)

我们可以修改响应的内容，欺骗客户端，本来响应的内容是当前所在的IP(134结尾)，我现在随意更改响应的内容（按`e`，底部提示我们修改的内容），然后再按`a`，将响应内容发送给客户端：

![](http://o7qrps1cr.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-06-15%20%E4%B8%8B%E5%8D%8810.15.24.png)

浏览器所受到的内容就是被我修改后的内容：

![](http://o7qrps1cr.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-06-15%20%E4%B8%8B%E5%8D%8810.16.07.png)