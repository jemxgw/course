# Git教程

> 本教程为[廖雪峰Git教程](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)依个人理解所精简

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

### 2.3 [管理修改](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/001374829472990293f16b45df14f35b94b3e8a026220c5000)

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

### 2.4 [撤销修改](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/001374831943254ee90db11b13d4ba9a73b9047f4fb968d000)

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

- 一种是`readme.txt`自修改后还没有被放到暂存区，也就是说还没有`add`，现在，撤销修改就回到和版本库一模一样的状态；
- 另一种是`readme.txt`已经添加到暂存区后，又作了修改，也就是说已经`add`了，现在，撤销修改就回到添加到暂存区后的状态。

总之，**`git checkout -- filename`就是让这个文件回到最近一次`git commit`或`git add`时的状态**。

`git checkout -- file`命令中的`--`很重要，没有`--`，就变成了“切换到另一个分支”的命令，我们在后面的分支管理中会再次遇到`git checkout`命令。

### 2.5 [删除文件](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013758392816224cafd33c44b4451887cc941e6716805c000)

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

## 3. [远程仓库](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/001374385852170d9c7adf13c30429b9660d0eb689dd43a000)

像国外的[github](https://github.com/)、[bitbucket](https://bitbucket.org/)、[gitlab](https://gitlab.com/)以及国内的[码云](https://git.oschina.net/)等等都是远程仓库。

### 3.1 [添加远程库](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013752340242354807e192f02a44359908df8a5643103a000)

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

### 3.2 [从远程库克隆](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/001375233990231ac8cf32ef1b24887a5209f83e01cb94b000)

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

Git支持多种协议，默认的`git://`使用ssh，但也可以使用`https`等其他协议。通过`ssh`支持的原生`git`协议速度最快。

在上一节中我们使用`https`协议将本地仓库与远程仓库关联，本节我们通过ssh将远程仓库克隆到本地。格式像这样：

https:

```
https://github.com/<your_user_name>/<repository_name>.git
```

ssh:

```
git@github.com:<your_user_name>/<repository_name>.git
```

如果通过ssh，需要在本地创建秘钥对：

```bash
$ cd .ssh
$ ssh-keygen -t rsa -C "youremail@example.com"
```

默认生成`id_rsa`和`id_rsa.pub`两个文件，这两个就是SSH Key的秘钥对。`id_rsa`是私钥，不能泄露出去，`id_rsa.pub`是公钥，可以放心地告诉任何人。

然后把`id_rsa.pub`文件中的内容添加到github的`Personal settings > SSH and GPG keys`中。

## 4. [分支管理](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013743862006503a1c5bf5a783434581661a3cc2084efa000)

### 4.1 [创建与合并分支](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/001375840038939c291467cc7c747b1810aab2fb8863508000)

Git鼓励大量使用分支：

- 查看分支：`git branch`
- 创建分支：`git branch <name>`
- 切换分支：`git checkout <name>`
- 创建+切换分支：`git checkout -b <name>`
- 合并某分支到当前分支：`git merge <name>`
- 删除分支：`git branch -d <name>`

我们的每一次提交串成了一条时间线，我们之前的所有的操作都是在master主分支上。`HEAD`指向的是当前分支，即master。

![](http://www.liaoxuefeng.com/files/attachments/0013849087937492135fbf4bbd24dfcbc18349a8a59d36d000/0)

当我们创建新的分支，例如`dev`时，Git新建了一个指针叫`dev`，指向`master`相同的提交，再把`HEAD`指向`dev`，就表示当前分支在`dev`上：

![](http://www.liaoxuefeng.com/files/attachments/001384908811773187a597e2d844eefb11f5cf5d56135ca000/0)

如果我们要把`dev`合并到`master`上，其实就是把`master`指向`dev`的当前提交：

![](http://www.liaoxuefeng.com/files/attachments/00138490883510324231a837e5d4aee844d3e4692ba50f5000/0)

**`git branch`**可以查看当前有哪些分支，\*星号标记的地方指的是当前所在的分支：

```bash
$ git branch
* master
```

我们也可以通过`git branch`新建分支，`git checkout`将分支切换到dev(在之前的章节中我们使用`git checkout -- filename`用于撤销更改)：

```bash
$ git branch dev
$ git branch
  dev
* master
$ git checkout dev
Switched to branch 'dev'
```

上面的命令还可以简化成：

```bash
$ git checkout -b dev
Switched to a new branch 'dev'
```

现在我们已经切换到dev分支，对readme.txt文件进行更改，在末行加入：

```
Creating a new branch is quick.
```

然后添加、提交：

```bash
$ git add -A
$ git commit -m "branch test"
[dev 62259c7] branch test
 1 file changed, 1 insertion(+)
```

我们现在切换回master分支会发现我们之前所做的更改没有生效，因为我们所做的更改是在dev分支上完成的，要使其生效，就需要把dev分支合并到master分支：

```bash
$ git merge dev
Updating 233a67a..62259c7
Fast-forward
 readme.txt | 1 +
 1 file changed, 1 insertion(+)
```

合并完成后，如果dev分支没用了就可以删除该分支了：

```bash
$ git branch -d dev
Deleted branch dev (was 62259c7).
$ git branch
* master
```

### 4.2 [解决冲突](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/001375840202368c74be33fbd884e71b570f2cc3c0d1dcf000)

我们现在新建一个分支：

```bash
$ git checkout -b feature1
Switched to a new branch 'feature1'
```

在readme.txt末尾加入一行，然后添加、提交：

```
Creating a new branch is quick AND simple.
```

```bash
$ git add .
$ git commit -m "AND simple"
[feature1 b5989d7] AND simple
 1 file changed, 1 insertion(+)
```

> `git add .` = `git add --all` = `git add -A`

然后回到主分支，对readme.txt再进行修改，加上一行：

```
Creating a new branch is quick & simple.
```

```bash
$ git add .
$ git commit -m "& simple"
```

现在分支master和feature1都有了各自的提交：

![](http://www.liaoxuefeng.com/files/attachments/001384909115478645b93e2b5ae4dc78da049a0d1704a41000/0)

我们现在尝试将两个分支合并：

```bash
$ git merge feature1
Auto-merging readme.txt
CONFLICT (content): Merge conflict in readme.txt
Automatic merge failed; fix conflicts and then commit the result.
```

Git告诉我们两个分支冲突了。

查看readme.txt的内容，Git用`<<<<<<<`，`=======`，`>>>>>>>`标记出不同分支的内容：

```bash
$ cat readme.txt
Git is a distributed version control system.
Git is free software distributed under the GPL.
Git has a mutable index called stage.
Git tracks changes of files.
Thie is a test repository.
<<<<<<< HEAD
Creating a new branch is quick & simple.
=======
Creating a new branch is quick AND simple.
>>>>>>> feature1

```

我们现在再次在master上修改readme.txt，将最后一行改成：

```
Creating a new branch is quick and simple.
```

添加、提交，再合并：

```bash
$ git add .
$ git commit -m "conflict fixed"
[master 55b09f9] conflict fixed
$ git merge feature1
Already up-to-date.
$ git status
On branch master
Your branch is ahead of 'origin/master' by 3 commits.
  (use "git push" to publish your local commits)
nothing to commit, working tree clean
```

现在，`master`分支和`feature1`分支变成了下图所示：

![](http://www.liaoxuefeng.com/files/attachments/00138490913052149c4b2cd9702422aa387ac024943921b000/0)

用带参数的`git log`也可以看到分支的合并情况，`--graph`顾名思义表示以形式展现：

```bash
$ git log --graph --pretty=oneline --abbrev-commit
*   55b09f9 conflict fixed
|\  
| * b5989d7 AND simple
* | b4d3c6c & simple
|/  
* 233a67a git push test
* 4a62c20 remove test.txt
* a32daca add test.txt
* 7d543eb git tracks changes2
* 84dd1e4 git tracks changes
* df40f20 understand how stage works
* aaa6df4 add GPL
* a08ee80 add distributed
* 56e96d1 wrote test files
* fe3df62 wrote test files
* 4bec9d6 wrote a readme file
```

最后，删除`feature1`分支：

```bash
$ git branch -d feature1
Deleted branch feature1 (was b5989d7).
$ git branch
* master
```

### 4.3 [分支管理策略](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013758410364457b9e3d821f4244beb0fd69c61a185ae0000)

- `git merge --no-ff ` 会在merge时生成一个新的commit

在4.1中，我们用`Fast forward`模式合并分支，但这种模式下，删除分支后，会丢掉分支信息。

如果要强制禁用`Fast forward`模式，Git就**会在merge时生成一个新的commit**，这样，从分支历史上就可以看出分支信息。

下面我们实战一下`--no-ff`方式的`git merge`：

首先我们还是新建一个dev分支，然后修改readme.txt文件，在添加、提交：

```bash
$ git checkout -b dev
Switched to a new branch 'dev'
 git branch
* dev
  master
$ vim readme.txt
$ git add .
$ git commit -m "add merge"
[dev 65ab232] add merge
 1 file changed, 1 insertion(+)
$ git checkout master
Switched to branch 'master'
Your branch is ahead of 'origin/master' by 3 commits.
  (use "git push" to publish your local commits)
```

准备合并`dev`分支，请注意`--no-ff`参数，表示禁用`Fast forward`：

```bash
$ git merge --no-ff -m "merge with no-ff" dev
Merge made by the 'recursive' strategy.
 readme.txt | 1 +
 1 file changed, 1 insertion(+)
$ git log --oneline --graph --abbrev-commit
*   753a911 merge with no-ff
|\  
| * 65ab232 add merge
|/  
*   55b09f9 conflict fixed
|\  
| * b5989d7 AND simple
* | b4d3c6c & simple
|/  
* 233a67a git push test
* 4a62c20 remove test.txt
* a32daca add test.txt
* 7d543eb git tracks changes2
* 84dd1e4 git tracks changes
* df40f20 understand how stage works
* aaa6df4 add GPL
* a08ee80 add distributed
* 56e96d1 wrote test files
* fe3df62 wrote test files
* 4bec9d6 wrote a readme file

```

可以看到，不使用`Fast forward`模式，merge后就像这样：

![](http://www.liaoxuefeng.com/files/attachments/001384909222841acf964ec9e6a4629a35a7a30588281bb000/0)

在实际开发中，我们应该按照几个基本原则进行分支管理：

- `master`分支应该是非常稳定的，也就是仅用来发布新版本，平时不能在上面干活；
- 在各dev分支上干活，也就是说，`dev`分支是不稳定的，到某个时候，比如1.0版本发布时，再把`dev`分支合并到`master`上，在`master`分支发布1.0版本；团队中的每个人都在`dev`分支上干活，每个人都有自己的分支，时不时地往`dev`分支上合并就可以了。

所以，团队合作的分支看起来就像这样：



![](http://www.liaoxuefeng.com/files/attachments/001384909239390d355eb07d9d64305b6322aaf4edac1e3000/0)

### 4.4 [Bug分支](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/00137602359178794d966923e5c4134bc8bf98dfb03aea3000)

- `git stash`
- `git stash list`
- `git stash apply`
- `git stash drop`
- `git stash pop`

比如我今天在dev上干活，干着干着，突然有个bug要修复，但是我在dev分支上的工作还没完成，那怎么办呢？Git提供了`git stash`功能，可以把我们在当前分支上的工作先储藏起来，待其他工作完成后，可以再恢复这个之前储藏起来的任务。

我们在分支dev上随便做些什么：

```bash
$ git branch
* dev
  master
$ vim readme.txt
$ git stash
Saved working directory and index state WIP on dev: 753a911 merge with no-ff
HEAD is now at 753a911 merge with no-ff
$ git status
On branch dev
nothing to commit, working tree clean
```

`git status`查看工作区显示nothing to commit。

比如，今天我们master分支上有一个bug要修改，我们先转到master分支，然后在master分支上新建一个issue101的分支用于处理bug，然后将修改后的issue101分支合并至master分支，最后再删除`issue101`分支

```bash
$ git branch
  dev
* master
$ git checkout -b issue101
M	readme.txt
Switched to a new branch 'issue101'
$ vim readme.txt
$ git status
On branch issue101
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	modified:   readme.txt

$ git add .
$ git commit -m "fix bug 101" 
[issue101 2f6254b] fix bug 101
 1 file changed, 1 insertion(+), 2 deletions(-)
$ git checkout master
Switched to branch 'master'
Your branch is ahead of 'origin/master' by 5 commits.
  (use "git push" to publish your local commits)
$ git merge --no-ff -m "merged bug fix 101" issue101
Merge made by the 'recursive' strategy.
 readme.txt | 3 +--
 1 file changed, 1 insertion(+), 2 deletions(-)
$ git branch -d issue101
Deleted branch issue101 (was 2f6254b).
$ git branch
  dev
* master
```

然后我们回到刚才工作的分支dev，那么刚才被我们储藏起来的工作区在哪里呢？这时候就可以用**`git stash list`**查看：

```bash
$ git stash list
stash@{0}: WIP on dev: 753a911 merge with no-ff
```

接下来我们就要回复刚才的工作区，恢复刚才的工作区有两种办法：

- 一是用`git stash apply`恢复，但是恢复后，stash内容并不删除，你需要用`git stash drop`来删除；
- 另一种方式是用`git stash pop`，恢复的同时把stash内容也删了。

```bash
$ git stash pop
On branch dev
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   readme.txt

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (d8dfd081baea0d35dd2fab454c56d141e3ce8d7d)
```

再用`git stash list`查看，就看不到任何stash内容了：

```bash
$ git stash list
```

你可以多次stash，恢复的时候，先用`git stash list`查看，然后用`git stash apply`恢复指定的stash：

```bash
$ git stash apply stash@{0}
```

### 4.5 [Feature分支](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/001376026233004c47f22a16d1f4fa289ce45f14bbc8f11000)

- `git branch -D <name>` 强制删除分支

feature分支和bug分支是类似的，创建，修改，合并，然后删除。

但是万一这新建的功能半路被老板kill掉了呢？如果新修改的分支在被合并前删除掉，Gi会提醒，该分支还没有被合并，如果删除，将丢失掉修改，如果要强行删除，需要使用命令`git branch -D <name>`。

### 4.6 [多人协作](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013760174128707b935b0be6fc4fc6ace66c4f15618f8d000)

- `git remote -v` 查看远程库信息
- `git push origin branch-name` 推送分支
- `git checkout -b branch-name origin/branch-name` 从本地创建与远程分支对应的分支
- `git branch --set-upstream branch-name origin/branch-name` 建立本地分支和远程分支的关联
- `git pull` 从远程抓取分支

当你从远程仓库克隆时，实际上Git自动把本地的`master`分支和远程的`master`分支对应起来了，并且，远程仓库的默认名称是`origin`。

#### 推送分支

分支推送建议：

- `master`分支是主分支，因此要时刻与远程同步；
- `dev`分支是开发分支，团队所有成员都需要在上面工作，所以也需要与远程同步；
- bug分支只用于在本地修复bug，没必要推到远程了；
- feature分支是否推到远程，取决于你是否和你的小伙伴合作在上面开发。

#### 抓取分支

默认情况下，从远程仓库克隆只能看到master分支，即origin分支，如果要在其他分支上开发，就要创建远程`origin`的`dev`分支到本地：

```bash
$ git checkout -b dev origin/dev
```

然后就可以在dev分支上更改，再提交，再push到远程仓库：

```bash
$ git commit -m "add /usr/bin/env"
[dev 291bea8] add /usr/bin/env
 1 file changed, 1 insertion(+)
$ git push origin dev
Counting objects: 5, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 349 bytes, done.
Total 3 (delta 0), reused 0 (delta 0)
To git@github.com:michaelliao/learngit.git
   fc38031..291bea8  dev -> dev
```

如果小组的两个人碰巧同时对一个文件做了更改，那么后推送的小伙伴的推送可能会冲突，那么就需要先`git pull`最新的提交下来，在本地合并，解决冲突再推送。如果`git pull`失败，则可能是因为没有指定本地`dev`分支与远程`origin/dev`分支的链接，要设置本地`dev`分支与远程`origin/dev`分支的链接：

```bash
$ git branch --set-upstream dev origin/dev
Branch dev set up to track remote branch dev from origin.
```

pull成功后，如果有冲突，解决完冲突就可以，提交，再push到远程仓库了。

#### 总结

**多人协作的工作模式**通常是这样：

1. 首先，可以试图用`git push origin branch-name`推送自己的修改；
2. 如果推送失败，则因为远程分支比你的本地更新，需要先用`git pull`试图合并；
3. 如果合并有冲突，则解决冲突，并在本地提交；
4. 没有冲突或者解决掉冲突后，再用`git push origin branch-name`推送就能成功！

如果`git pull`提示“no tracking information”，则说明本地分支和远程分支的链接关系没有创建，用命令`git branch --set-upstream branch-name origin/branch-name`。

## 5. [标签管理](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013762144381812a168659b3dd4610b4229d81de5056cc000)

Git的标签是版本库的快照，其实它就是指向某个commit的指针（跟分支很像，但是分支可以移动，标签不能移动），所以，创建和删除标签都是瞬间完成的。

**为什么还要引入tag**？

> “请把上周一的那个版本打包发布，commit号是6a5819e...”
>
> “一串乱七八糟的数字不好找！”
>
> 如果换一个办法：
>
> “请把上周一的那个版本打包发布，版本号是v1.2”
>
> “好的，按照tag v1.2查找commit就行！”
>
> 所以，tag就是一个让人容易记住的有意义的名字，它跟某个commit绑在一起。

### 5.1 [创建标签](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/001376951758572072ce1dc172b4178b910d31bc7521ee4000)

- `git tag <tag-name> <commit-id>` 创建标签

要创建标签，先切换到要创建标签的分支，**默认对最新的commit即HEAD创建标签**：

```bash
$ git branch
* master
$ git tag v1.0
$ git tag
v1.0
```

也可以**指定commit id**来创建标签：

```bash
$ git log --pretty=oneline --abbrev-commit
8181f44 add .ignore
316085e Merge branch 'dev'
8b16086 fix bug
ce2467c merged bug fix 101
2f6254b fix bug 101
753a911 merge with no-ff
65ab232 add merge
55b09f9 conflict fixed
b4d3c6c & simple
b5989d7 AND simple
233a67a git push test
4a62c20 remove test.txt
a32daca add test.txt
7d543eb git tracks changes2
84dd1e4 git tracks changes
df40f20 understand how stage works
aaa6df4 add GPL
a08ee80 add distributed
56e96d1 wrote test files
fe3df62 wrote test files
4bec9d6 wrote a readme file
$ git tag v0.9 3160
$ git tag
v0.9
v1.0
```

可以通过`git show`来显示标签的说明：

```bash
$ git show v0.9
commit 316085e7001fcddd87dd0a731e1df181a36febae
Merge: ce2467c 8b16086
Author: zhangmimi <mimizhang12345@163.com>
Date:   Mon May 1 20:34:10 2017 +0800

    Merge branch 'dev'

```

也可以指定标签信息：

```bash
$ git tag -a v0.1 -m "initial commit" 4bec9d6
$ git show v0.1
tag v0.1
Tagger: zhangmimi <mimizhang12345@163.com>
Date:   Wed May 3 15:35:27 2017 +0800

initial commit

commit 4bec9d601c8f9a2b8239c2435fb1f2f60cedd215
Author: zhangmimi <mimizhang12345@163.com>
Date:   Wed Apr 26 21:10:38 2017 +0800

    wrote a readme file

diff --git a/readme.txt b/readme.txt
new file mode 100644
index 0000000..46d49bf
--- /dev/null
+++ b/readme.txt
@@ -0,0 +1,2 @@
+Git is a version control system.
+Git is free software.
```

### 5.2 操作标签

- `git tag -d` 本地删除标签
- `git push origin :refs/tags/<version-name>` 删除远程标签
- `git push origin <version-name>`  将标签推送至远程仓库
- `git push origin --tags`  推送全部未推送过的本地标签

如果标签打错了，还没有推送到远程仓库，就可以本地删除该标签：

```bash
$ git tag -d v0.1
Deleted tag 'v0.1' (was fe55708)
$ git tag
v0.9
v1.0
```

如果该标签已经推送到远程仓库，先要从本地删除，然后再删除线上的标签：

```bash
$ git tag -d v1.0
Deleted tag 'v1.0' (was 8181f44)
$ git push origin :refs/tags/v1.0
To https://github.com/mimizhang/learngit.git
 - [deleted]         v1.0
```

可在github上的releases上查看标签是否删除：

![](http://o7qrps1cr.bkt.clouddn.com/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202017-05-03%20%E4%B8%8B%E5%8D%884.21.20.png)

将本地的标签推送至远程仓库：

```bash
$ git push origin v0.9
Total 0 (delta 0), reused 0 (delta 0)
To https://github.com/mimizhang/learngit.git
 * [new tag]         v0.9 -> v0.9
$ git push origin --tags
```

## 6. 自定义Git

- `git config --global color.ui true` 让Git显示颜色

### 6.1 [忽略特殊文件](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013758404317281e54b6f5375640abbb11e67be4cd49e0000)

- 可以借鉴[.gitignore文件模板](https://github.com/github/gitignore)来更改.gitignore文件；

- 忽略某些文件时，需要编写`.gitignore`；

- `.gitignore`文件本身要放到版本库里，并且可以对`.gitignore`做版本管理；

- `.gitignore`写错了，可以用`git check-ignore`命令检查

  ```bash
  $ git check-ignore -v App.class
  .gitignore:3:*.class    App.class
  ```

**忽略文件的原则是**：

1. 忽略操作系统自动生成的文件，比如缩略图等；
2. 忽略编译生成的中间文件、可执行文件等，也就是如果一个文件是通过另一个文件自动生成的，那自动生成的文件就没必要放进版本库，比如Java编译产生的`.class`文件；
3. 忽略你自己的带有敏感信息的配置文件，比如存放口令的配置文件。

### 6.2 [配置别名](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/001375234012342f90be1fc4d81446c967bbdc19e7c03d3000)

可以对git命令配置别名，比如我们把`status`命令的别名设置成`st`：

```bash
$ git config --global alias.st status
$ git st
On branch master
Your branch is up-to-date with 'origin/master'.
nothing to commit, working tree clean
```

`--global`参数表示对当前用户都生效，如果不加，只对当前的仓库起作用。

每个仓库的Git**配置文件**都放在`.git/config`文件中，而当前用户的Git配置文件放在用户主目录下的一个隐藏文件`.gitconfig`中。