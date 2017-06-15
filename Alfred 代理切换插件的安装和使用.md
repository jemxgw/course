# Alfred 代理切换插件的安装和使用

proxy-switcher-alfred-workflow是在Alfred基础上的代理切换插件，项目主页：https://github.com/lululau/proxy-switcher-alfred-workflow

## 要求：

前提当然是得安装Alfred。

## 安装步骤：

到项目主页下载`ProxySwitcher.alfredworkflow`文件，打开它，将他导入到ALfred中。

## 使用：

新建`.proxyswitcher.rc`文件到主目录下，根据以下格式编辑文件，然后在Alfred中输入`proxy`即可根据`.proxyswitcher.rc`的配置切换代理。

```yaml
AutoDiscoveryProxy:   # AutoDiscoveryProxy has no options
AutoProxy:
  URL: "file://localhost/Applications/Safari.app/Contents/Resources/autoproxy.pac"  # URL of pac file
SocksProxy:
  Host: 127.0.0.1
  Port: 8080
  Auth: true
  Username: hello
  Password: 123123
HTTPProxy:
  Host: 127.0.0.1
  Port: 8080
  Auth: false
HTTPSProxy:
  Host: 127.0.0.1
  Port: 8080
  Auth: false
FTPProxy:
  Host: 127.0.0.1
  Port: 8080
  Auth: false
RTSPProxy:
  Host: 127.0.0.1
  Port: 8080
  Auth: false
GopherProxy:
  Host: 127.0.0.1
  Port: 8080
  Auth: false
```

![](http://o7qrps1cr.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-06-13%20%E4%B8%8B%E5%8D%888.30.50.png)

