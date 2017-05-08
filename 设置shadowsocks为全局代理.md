# 设置shadowsocks为全局代理

> 以下仅针对mac用户

从VPN转为shadowsocks翻墙之后，最大的困惑是socks5只是局部代理，不能像VPN那样把整个电脑都代理（VPN和shadowsocks的区别可以[参考这里](https://doub.io/ss-jc9/)）。就拿我们做爬虫来说，最常接触的就是浏览器，抓包工具和写脚本，但是会发现只有浏览器能够走socks5，也就是说你要爬一个被墙的网站，浏览器能够访问，但是写的脚本无法访问，抓包工具charlse也无法录制到数据（当然在脚本中设置代理或者在charles中设置外部代理也可以实现相同的效果，但不免有点繁琐）。因此我们要想办法把shadowsocks设置为全局代理。在这里我们可以使用[Proxifier](https://www.proxifier.com/)（[下载](https://pan.baidu.com/s/1eQ1tD9g)）把shadowsocks代理转为全局代理。

## 1. **设置代理服务器**

安装好Proxifier，点击Profile >> Proxy Servers 可以看到下面的界面（下图已经有一条代理设置，点击Add后填上相应的地址和端口（shadowsocks默认端口是1080）以及协议的形式保存即可）：

![](http://o7qrps1cr.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-05-08%20%E4%B8%8B%E5%8D%883.56.05.png)

![](http://o7qrps1cr.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-05-08%20%E4%B8%8B%E5%8D%884.04.40.png)

## 2. 开启远程dns解析

为了防止DNS污染，DNS设置为使用远程服务器的DNS设置：

![](http://o7qrps1cr.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-05-08%20%E4%B8%8B%E5%8D%884.05.40.png)

以上两步简单的设置即可实现全局代理，你可以通过Charles录制到走sock5协议的数据，终端也可翻墙。

## 3. 附：不通过Proxifier设全局代理，实现charles抓包和python设置requests代理

### 3.1 charles设置外部代理

Proxy >> External Proxy Settings 

地址和端口对应的是shaodowsocks偏好设置中的HTTP代理监听的地址和端口：

![](http://o7qrps1cr.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-05-08%20%E4%B8%8B%E5%8D%888.15.56.png)

![](http://o7qrps1cr.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-05-08%20%E4%B8%8B%E5%8D%888.27.57.png)

设置完后重启Charles，Charles即可录包。

这样设置Charles，不仅Charles可实现捕捉走socks协议的数据，而且也可实现全局代理，在终端上也可实现翻墙。

### 3.2 Python requests包设置代理

以下引用至[官方文档](http://cn.python-requests.org/zh_CN/latest/user/advanced.html#proxies)：

> 除了基本的 HTTP 代理，Requests 还支持 SOCKS 协议的代理。这是一个可选功能，若要使用， 你需要安装第三方库。
> 你可以用 pip 获取依赖:
>
> ```bash
> $ pip install requests[socks]
> ```
> 安装好依赖以后，使用 SOCKS 代理和使用 HTTP 代理一样简单：
> ```python
> proxies = {
>     'http': 'socks5://user:pass@host:port',
>     'https': 'socks5://user:pass@host:port'
> }
> ```

**举个例子**：

当我们使用shadowsocks代理时，shadowsocks会自动修改系统代理设置，代理地址可从**网络偏好设置**中查看：

![](http://o7qrps1cr.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-05-08%20%E4%B8%8B%E5%8D%8810.03.30.png)

```python
import requests

proxies = {
    'https': 'socks5://127.0.0.1:1080',
    'http': 'socks5://127.0.0.1:1080'
}

response = requests.get('https://www.google.com/', proxies=proxies, verify=False)
```


