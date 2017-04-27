# Git教程

> 本教程为[廖雪峰Git教程](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)依个人理解的总结

## 1. [创建版本库](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013743256916071d599b3aed534aaab22a0db6c4e07fd0000)repository

- `git init`
- `git status`
- `git add`
- `git commit`

首先，来到`learngit`目录下，开始我们的Git旅程。**`git init`**命令把这个目录变成Git可以管理的仓库:

```bash
$ cd learngit
$ git init
```

新建一个readme.txt文本文件,在上面随便写点什么,然后保存：

```bash
$ vim readme.txt
$ ls -a
.		..		.git		readme.txt
```

**`git status`**查看这个版本库的状态:

```bash
$ git status
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	readme.txt

nothing added to commit but untracked files present (use "git add" to track)
```

**`git add`**告诉Git，把文件添加到仓库:

```bash
$ git add readme.txt
$ git status
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   readme.txt

```

**`git commit`**告诉Git，把文件提交到仓库，**`-m`**后面输入的是本次提交的说明:

```bash
$ git commit -m "wrote a readme file" 
[master (root-commit) 4bec9d6] wrote a readme file
 1 file changed, 2 insertions(+)
 create mode 100644 readme.txt
$ git status
On branch master
nothing to commit, working tree clean
```

可以多次`add`不同的文件，然后再`commit`,**`--all`**参数添加所有文件:

```bash
$ vim readme2.txt
$ vim readme3.txt
$ git add readme2.txt readme3.txt
$ git commit -m "wrote test files"
[master fe3df62] wrote test files
 2 files changed, 2 insertions(+)
 create mode 100644 readme2.txt
 create mode 100644 readme3.txt
$ vim readme4.txt
$ vim readme5.txt
$ git add --all
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   readme4.txt
	new file:   readme5.txt

$ git commit -m "wrote test files"
[master 56e96d1] wrote test files
 2 files changed, 2 insertions(+)
 create mode 100644 readme4.txt
 create mode 100644 readme5.txt
$ git status
On branch master
nothing to commit, working tree clean
```

## 2. [时光机穿梭](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013743858312764dca7ad6d0754f76aa562e3789478044000)

- `git diff`

现在我们修改一下readme.txt文件

```bash
$ vim readme.txt
```

修改成:

```
Git is a distributed version control system.
Git is free software.
```

查看仓库的状态:

```bash
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   readme.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

**`git diff`**查看修改前后的异同，`diff`即difference:

```bash
$ git diff
diff --git a/readme.txt b/readme.txt
index 46d49bf..9247db6 100644
--- a/readme.txt
+++ b/readme.txt
@@ -1,2 +1,2 @@
-Git is a version control system.
+Git is a distributed version control system.
 Git is free software.
```

然后添加、提交:

```bash
$ git add readme.txt
$ git commit -m "add distributed"
[master a08ee80] add distributed
 1 file changed, 1 insertion(+), 1 deletion(-)
```

### 2.1 [版本回退](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013744142037508cf42e51debf49668810645e02887691000)

- `git log`
- `git reset`
- `git reflog`

修改readme.txt文件如下：

```
Git is a distributed version control system.
Git is free software distributed under the GPL.
```

然后添加、提交：

```bash
$ git add --all
$ git commit -m "add GPL"
```

我们对readme.txt已经进行了多次修改，**`git log`**命令可以显示从最近到最远的提交日志，我们可以看到最近的一次提交:`add GPL`：

```bash
$ git log
commit aaa6df4bef9fa8b9a64dcfb4f4b3c35800cf9c95
Author: zhangmimi <mimizhang12345@163.com>
Date:   Thu Apr 27 09:42:32 2017 +0800

    add GPL

commit a08ee808a3ac1845a5af9624c5ea99873d249dd6
Author: zhangmimi <mimizhang12345@163.com>
Date:   Wed Apr 26 23:18:45 2017 +0800

    add distributed

commit 56e96d1f46f51cd65e87fa0adc03c2d3ffc5ec18
Author: zhangmimi <mimizhang12345@163.com>
Date:   Wed Apr 26 22:49:05 2017 +0800

    wrote test files

commit fe3df622c0f330733b7a7a0a316c92960df81ad4
Author: zhangmimi <mimizhang12345@163.com>
Date:   Wed Apr 26 22:45:40 2017 +0800

    wrote test files

```

实际工作中，我们可能提交了多次的修改，如果这样输出会觉得眼花缭乱，可以添加**`--pretty=oneline`**参数，每一行只显示`commit id`和`commit 说明`：

```bash
$ git log --pretty=oneline
aaa6df4bef9fa8b9a64dcfb4f4b3c35800cf9c95 add GPL
a08ee808a3ac1845a5af9624c5ea99873d249dd6 add distributed
56e96d1f46f51cd65e87fa0adc03c2d3ffc5ec18 wrote test files
fe3df622c0f330733b7a7a0a316c92960df81ad4 wrote test files
4bec9d601c8f9a2b8239c2435fb1f2f60cedd215 wrote a readme file
```

如果我们想要回退到上一个版本，即`add distributed`要怎么做呢？

想要回退到上一个版本，那就要让Git知道具体是哪一个版本。`HEAD`表示当前版本，`HEAD^`表示当前版本的上一个版本。上上一个版本就是`HEAD^^`，当然往上100个版本写100个`^`比较容易数不过来，所以写成`HEAD~100`。而回退命令是**`git reset`**:（`--hard`后面会提到）

```bash
$ git reset --hard HEAD^
HEAD is now at a08ee80 add distributed
```

然后我们再看看readme.txt文件现在是什么样子：

```bash
$ cat readme.txt
Git is a distributed version control system.
Git is free software.
```

通过`~2`回退到上上个版本：

```bash
$ git reset --hard HEAD~2
HEAD is now at fe3df62 wrote test files
$ git log
commit fe3df622c0f330733b7a7a0a316c92960df81ad4
Author: zhangmimi <mimizhang12345@163.com>
Date:   Wed Apr 26 22:45:40 2017 +0800

    wrote test files

commit 4bec9d601c8f9a2b8239c2435fb1f2f60cedd215
Author: zhangmimi <mimizhang12345@163.com>
Date:   Wed Apr 26 21:10:38 2017 +0800

    wrote a readme file

```

除了通过`HEAD`的方式回到过去，我们还可以指定`commit id`回到过去。

Git提供了一个命令**`git reflog`**用来记录你的每一次命令：

```bash
$ git reflog
fe3df62 HEAD@{0}: reset: moving to HEAD~2
a08ee80 HEAD@{1}: reset: moving to HEAD^
aaa6df4 HEAD@{2}: commit: add GPL
a08ee80 HEAD@{3}: commit: add distributed
56e96d1 HEAD@{4}: commit: wrote test files
fe3df62 HEAD@{5}: commit: wrote test files
4bec9d6 HEAD@{6}: commit (initial): wrote a readme file
$ git reset --hard a08ee80
HEAD is now at a08ee80 add distributed
$ git reset --hard aaa6
HEAD is now at aaa6df4 add GPL
```

### 2.2 [工作区和暂存区](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013745374151782eb658c5a5ca454eaa451661275886c6000)

#### 工作区（Working Directory）

我们当前所在的`learngit`目录就是**工作区**：

```bash
$ ls
license		readme2.txt	readme4.txt
readme.txt	readme3.txt	readme5.txt
```

#### 版本库（Repository）

`learngit`目录下隐藏的`.git`文件就是**版本库**：

```bash
$ ls -a
.		.git		readme.txt	readme3.txt	readme5.txt
..		license		readme2.txt	readme4.txt
```

Git的版本库里存了很多东西，其中最重要的就是称为stage（或者叫index）的**暂存区**，还有Git为我们自动创建的第一个分支`master`，以及指向`master`的一个指针叫`HEAD`。

![](http://www.liaoxuefeng.com/files/attachments/001384907702917346729e9afbf4127b6dfbae9207af016000/0)

现在我们修改readme.txt，并且新建一个license文件

```bash
$ vim readme.txt
$ vim license
$ ls
license		readme2.txt	readme4.txt
readme.txt	readme3.txt	readme5.txt
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   readme.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	license

```

Git非常清楚地告诉我们，`readme.txt`被修改了，而`LICENSE`还从来没有被添加过，所以它的状态是`Untracked`。

现在，使用命令`git add -A`(或者`git add --all`)，把`readme.txt`和`LICENSE`都添加后，用`git status`再查看一下：

```bash
$ git add -A
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   license
	modified:   readme.txt

```

现在，暂存区的状态就变成这样了：

![](http://www.liaoxuefeng.com/files/attachments/001384907720458e56751df1c474485b697575073c40ae9000/0)

**`git add`命令实际上就是把要提交的所有修改放到暂存区（Stage），然后，执行`git commit`就可以一次性把暂存区的所有修改提交到分支。**

```bash
$ git commit -m "understand how stage works"
[master df40f20] understand how stage works
 2 files changed, 2 insertions(+)
 create mode 100644 license
$ git status
On branch master
nothing to commit, working tree clean
```

现在版本库变成了这样，暂存区就没有任何内容了：

![](http://www.liaoxuefeng.com/files/attachments/0013849077337835a877df2d26742b88dd7f56a6ace3ecf000/0)

### 2.3 管理修改

**Git跟踪并管理的是修改，而非文件。**

修改readme.txt文件，添加一行内容：

```
Git is a distributed version control system.
Git is free software distributed under the GPL.
Git has a mutable index called stage.
Git tracks changes.
```

然后添加：

```bash
$ git add readme.txt
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	modified:   readme.txt
```

然后，再修改readme.txt：

```
Git is a distributed version control system.
Git is free software distributed under the GPL.
Git has a mutable index called stage.
Git tracks changes of files.
```

提交：

```bash
$ git commit -m "git tracks changes"
[master 84dd1e4] git tracks changes
 1 file changed, 1 insertion(+)
```

提交后，再看看状态，会发现第二次的修改没有被提交。这就对了！**因为第二次的修改我们没有`add`到暂存区，`git commit`只负责把暂存区的修改提交了，也就是第一次的修改被提交了，第二次的修改不会被提交。**

```bash
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   readme.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

用`git diff HEAD -- readme.txt`命令可以查看工作区和版本库里面最新版本的区别：

```bash
$ git diff HEAD -- readme.txt
diff --git a/readme.txt b/readme.txt
index 76d770f..a9c5755 100644
--- a/readme.txt
+++ b/readme.txt
@@ -1,4 +1,4 @@
 Git is a distributed version control system.
 Git is free software distributed under the GPL.
 Git has a mutable index called stage.
-Git tracks changes.
+Git tracks changes of files.
```

我们可以再次`add`和`commit`：

```bash
$ git add --all
$ git commit -m "git tracks changes2"
[master 7d543eb] git tracks changes2
 1 file changed, 1 insertion(+), 1 deletion(-)
 $ git status
On branch master
nothing to commit, working tree clean
```

### 2.4 撤销修改

- `git checkout -- filename`

如果现在你对readme.txt文件做了很多更改，比如我骂了一下老板：

```
Git is a distributed version control system.
Git is free software distributed under the GPL.
Git has a mutable index called stage.
Git tracks changes of files.
My stupid boss still prefers SVN.
```

后来觉得这要是被老板看到就完蛋了，你想撤销现在的更改，当然，你可以删掉最后一行，手动把文件恢复到上一个版本的状态。但假如你修改了很多地方，你也要一个个修改吗？会不会觉得很麻烦，这个时候就可以用**`git checkout -- filename`**命令，然后你会发现文件恢复到修改之前的状态

```bash
$ git checkout -- readme.txt
$ cat readme.txt
Git is a distributed version control system.
Git is free software distributed under the GPL.
Git has a mutable index called stage.
Git tracks changes of files.
$ git status
On branch master
nothing to commit, working tree clean
```

命令`git checkout -- readme.txt`意思就是，把`readme.txt`文件在工作区的修改全部撤销，这里有两种情况：

一种是`readme.txt`自修改后还没有被放到暂存区，也就是说还没有`add`，现在，撤销修改就回到和版本库一模一样的状态；

一种是`readme.txt`已经添加到暂存区后，又作了修改，也就是说已经`add`了，现在，撤销修改就回到添加到暂存区后的状态。

总之，**`git checkout -- filename`就是让这个文件回到最近一次`git commit`或`git add`时的状态**。

`git checkout -- file`命令中的`--`很重要，没有`--`，就变成了“切换到另一个分支”的命令，我们在后面的分支管理中会再次遇到`git checkout`命令。

### 2.5 删除文件

- `git rm`

在Git中，删除也是一个修改操作。

我们先新建一个test.txt文件，然后添加、提交：

```bash
$ git add test.txt
$ git commit -m "add test.txt"
```

然后我们删除test.txt文件：

```bash
$ rm -f test.txt
```

然后查看一下版本库的状态，`git status`命令会立刻告诉我们哪些文件被删除了：

```bash
$ git status
On branch master
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	deleted:    test.txt
```

现在两种情况，一种是这个文件有用，但是被我们误删了，另一种是这个文件确实没用。

假如是误删，我们可以使用**`git checkout -- test.txt`**:

```bash
$ git checkout -- test.txt
$ git status
On branch master
nothing to commit, working tree clean
$ ls
license		readme2.txt	readme4.txt	test.txt
readme.txt	readme3.txt	readme5.txt
```

这个时候我们发现test.txt文件回来了。

另一种情况，我们真的要删除这个文件，但是刚才已经`commit`了，我们可以使用`git rm filename`：

```bash
$ git rm test.txt
rm 'test.txt'
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	deleted:    test.txt

$ git commit -m "remove test.txt"
[master 4a62c20] remove test.txt
 1 file changed, 0 insertions(+), 0 deletions(-)
 delete mode 100644 test.txt
$ git status
On branch master
nothing to commit, working tree clean
```

## 3. 远程仓库

像国外的[github](https://github.com/)、[bitbucket](https://bitbucket.org/)、[gitlab](https://gitlab.com/)以及国内的[码云](https://git.oschina.net/)等等都是远程仓库。

### 3.1 添加远程库

- `git remote add origin`
- `git push -u origin master`第一次推送master分支的所有内容

一开始我们在github上新建一个仓库，

然后在`learngit`目录下，**`git remote add origin`**后面跟上你的仓库地址，即可把本地仓库与远程仓库关联：

```bash
$ git remote add origin https://github.com/<your-github-username>/my-first-blog.git
```

远程库的名字就是`origin`，这是Git默认的叫法，也可以改成别的，但是`origin`这个名字一看就知道是远程库。

然后，把本地库的所有内容推送到远程库上：

```bash
$ git push -u origin master
Counting objects: 31, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (24/24), done.
Writing objects: 100% (31/31), 2.35 KiB | 0 bytes/s, done.
Total 31 (delta 12), reused 0 (delta 0)
remote: Resolving deltas: 100% (12/12), done.
To https://github.com/mimizhang/learngit.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.
```

把本地库的内容推送到远程，用**`git push`**命令，实际上是把当前分支`master`推送到远程。

由于远程库是空的，我们第一次推送`master`分支时，加上了`-u`参数，Git不但会把本地的`master`分支内容推送的远程新的`master`分支，还会把本地的`master`分支和远程的`master`分支关联起来，在以后的推送或者拉取时就可以简化命令。

比如我们现在再修改下readme.txt：

```
Git is a distributed version control system.
Git is free software distributed under the GPL.
Git has a mutable index called stage.
Git tracks changes of files.
Thie is a test repository.
```

然后添加、提交、再推送到远程仓库：

```bash
$ git add --all
$ git commit -m "git push test"
[master 233a67a] git push test
 1 file changed, 1 insertion(+)
$ git push
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 310 bytes | 0 bytes/s, done.
Total 3 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/mimizhang/learngit.git
   4a62c20..233a67a  master -> master

```

赶紧去看看github上对应的仓库有没有发生变化！

### 3.2 从远程库克隆

- `git clone`

上一节，我们是先有本地仓库，然后再同步到远程仓库，如果反过来呢？

比如我们在github上面新建一个gitskills仓库，那么如何把它克隆到本地呢？

```bash
$ git clone git@github.com:mimizhang/gitskills.git
Cloning into 'gitskills'...
remote: Counting objects: 3, done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.
$ cd gitskills
$ ls
README.md
```

Git支持多种协议，默认的`git://`使用ssh，但也可以使用`https`等其他协议。

在上一节中我们使用`https`协议将本地仓库与远程仓库关联，本节我们通过ssh将远程仓库克隆到本地。格式像这样：

https:

```
https://github.com/<your_user_name>/<repository_name>.git
```

ssh:

```
git@github.com:<your_user_name>/<repository_name>.git
```

如果通过