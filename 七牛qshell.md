# 七牛qshell

**qshell**是七牛API服务的命令行工具。但是我把它当做博客图床的图片上传工具。本篇文章仅介绍作为图片上传工具时常用的命令。因为笔者的工作环境是mac，所以也仅介绍在mac上的操作（当然，Linux上的操作也是类似的。）更多详细介绍请移步[官方文档](https://github.com/qiniu/qshell)。

## 1. 安装及配置

`qshell`文件可从[官方文档](https://github.com/qiniu/qshell)下载。下载后把文件名改为`qshell`。

为了让`qshell`可以在任何路径下运行，需要把`qshell`所在的目录加入到环境变量`$PATH`中去。假如我把`qshell`放在`/Users/qshell`路径下，我们需要在`~/.bashrc`中加入：

```bash
export PATH=$PATH:/Users/qshell
```

保存后输入`source ~/.bashrc`来使配置立即生效。

## 2. 添加账户密钥

使用`qshell account ak sk`可以添加账户密钥。ak对应AccessKey，sk对应SecretKey。添加了账户信息就可以下面的操作了。

## 3. 查看空间名称和域名

`qshell buckets`可以查看当前账号下所有的空间名称

```bash
$ qshell buckets
test1
test2
```

`qshell domains`获取指定空间的所有关联域名，下面的指定空间就是`test1`:

```bash
$ qshell domains test1 
XXXXXXX.bkt.clouddn.com
```

## 4. 上传文件

### 4.1 上传单个文件：`fput`

`fput`适合于中小型文件的上传。如果要上传大文件请使用`rput`命令，使用[分片上传](https://github.com/qiniu/qshell/blob/master/docs/rput.md)。

```bash
qshell fput <Bucket> <Key> <LocalFile>
```
`Bucket`为对应的七牛空间名称，`Key`为文件保存在七牛空间的名称，`LocalFile`为文件在本地的路径。

```bash
$ qshell fput work test.png /Users/Desktop/test.jpg
Uploading /Users/Desktop/test.jpg => work : test.png ...
Progress: 100%
Put file /Users/Desktop/test.jpg => work : test.png success!
Hash: xxxxxxxxxxxxxxx
Fsize: 42704 ( 41.70 KB )
MimeType: image/jpeg
Last time: 0.14 s, Average Speed: 303.2 KB/s
```

### 4.2 同步文件：`qupload`

`qupload`用来将本地目录中的文件同步到七牛空间

```bash
qshell qupload [<ThreadCount>] <LocalUploadConfig>
```

`ThreadCount`为携程数量，可以理解为同时上传多少个文件，比如`ThreadCount`设定为1，就是一个个上传文件；

`LocalUploadConfig`为数据同步的配置文件，最基本的配置如下：

```json
{
	"src_dir": "/Users/Desktop/capture",
	"bucket": "test"
}
```

`src_dir`为本地同步路径，为全路径格式，将同步该目录下面所有的文件;

`bucket`为目标七牛空间名称。

```bash
$ qshell qupload 1 /Users/qshell/work.conf
Writing upload log to file /Users/.qshell/qupload/8c88a3fffa7b9d2fc7f997ef65ed2334/8c88a3fffa7b9d2fc7f997ef65ed2334.log
Uploading /Users/Desktop/capture/屏幕快照 2017-08-22 下午9.38.14.png => 屏幕快照 2017-08-22 下午9.38.14.png [2/2, 100.0%] ...

See upload log at path /Users/zhangmimi/.qshell/qupload/8c88a3fffa7b9d2fc7f997ef65ed2334/8c88a3fffa7b9d2fc7f997ef65ed2334.log
```

## 5. 获取文件列表：`listbucket`

```
qshell listbucket [-marker <Marker>] <Bucket> [<Prefix>] <ListBucketResultFile>
```

`Bucket`：空间名称
`Prefix`：空间中的文件名前缀，如果不指定该参数则列出全部文件信息

`ListBucketResultFile`：如果该参数指定为`stdout`，则会把结果输出到终端

```bash
$ qshell listbucket test 屏幕快 stdout
屏幕快照 2016-10-12 下午4.22.27.png	175981	FngiNaL4WjtymSQBuTmB1NrOuGCb	14762606477081422	image/png	0	
屏幕快照 2017-02-04 下午3.56.31.png	28719	Fj8tOiTxAKCX4w4pmU-k8njMVyAT	14861950222714450	image/png	0	
屏幕快照 2017-02-04 下午4.37.12.png	27116	FuTGTo5NO_fGhkjiCXZwhLu5CTht	14861974479498973	image/png	0	
```

## 6. 删除文件：

### 6.1 删除单个文件：`delete`

```
qshell delete <Bucket> <Key>
```

`Bucket`：空间名称
`Key`：空间中的文件名

```bash
$ qshell delete test "屏幕快照 2017-02-04 下午5.05.42.png"
```

test为空间名称，"屏幕快照 2017-02-04 下午5.05.42.png"为空间中的文件名称。

### 6.2 批量删除：`batchdelete`

`batchdelete`命令用来根据一个七牛空间中的文件名列表来批量删除空间中的这些文件。

```
qshell batchdelete [-force] <Bucket> <KeyListFile>
```

`Bucket`：空间名称
`KeyListFile`：文件列表文件，是一个txt文件，样式如下：

```
a.jpg
test/b.jpg
```

`-force`：表示强制删除，不需要验证

```bash
$ qshell batchdelete test test.txt
<DANGER> Input hbcbhf to confirm operation: hbcbhf
```

