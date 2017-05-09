# GIT CHEAT SHEET

后续会根据工作中遇到的问题不断更新......

## 参考资料

Git常用命令速查表

[廖雪峰Git教程](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)

[官方文档](https://git-scm.com/book/zh/v2)

[图解Git](http://marklodato.github.io/visual-git-guide/index-zh-cn.html)([英文版](http://marklodato.github.io/visual-git-guide/index-en.html))

[Git的奇技淫巧](https://github.com/521xueweihan/git-tips)([英文版](https://github.com/git-tips/tips))

[TOWER GIT CHEAT SHEET](https://pan.baidu.com/s/1slLL2PJ)

## 创建

| 命令                                       | 说明         |
| ---------------------------------------- | ---------- |
| `git clone ssh://user@domain.com/repo.git` | 将远处仓库克隆至本地 |
| `git init`                               | 创建本地Git仓库  |

## 本地修改

| 命令                              | 说明                                       |
| ------------------------------- | ---------------------------------------- |
| `git status`                    | 查看当前仓库的状态                                |
| `git diff`                      | 查看文件修改前后的异同                              |
| `git add .`                     | 将所有文件的更改提交到暂存区                           |
| `git add -p <file> `            | 将文件file的更改提交到暂存区                         |
| `git commit -m`                 | 将暂存区的文件提交至仓库(`-m`参数是提交的说明)               |
| `git commit -a`                 | 将当前目录下的所有文件的所有更改提交至仓库(`add`和`commit`一起操作) |
| `git commit --amend <file> -m ` | 修改上一个commit的描述                           |
| `git stash`                     | 存储当前的修改                                  |
| `git stash list`                | 展示所有stashes                              |
| `git stash apply <stash@{n}>`   | 回到某个stash的状态                             |
| `git stash pop`                 | 回到最后一个stash的状态，并删除这个stash                |
| `git stash clear`               | 删除所有的stash                               |

## 提交历史

| 命令                  | 说明                                 |
| ------------------- | ---------------------------------- |
| `git log`           | 显示所有提交日志(由近至远排序)                   |
| `git log -p <file>` | 显示某个文件的提交日志                        |
| `git blame <file>`  | 显示文件的操作人、操作时间和具体的操作(who,when,what) |
| `git reflog`        | 显示本地执行过的git命令                      |

## 分支和标签

| 命令                        | 说明                     |
| ------------------------- | ---------------------- |
| `git branch -av`          | 列出所有分支的信息包括与远程库对应的分支信息 |
| `git checkout <branch>`   | 切换分支                   |
| `git branch <new-branch>` | 创建分支                   |
| `git branch -d <branch>`  | 删除本地分支                 |
| `git tag <tag-name>`      | 对最新的commit即HEAD创建标签    |

## 更新和发布

| 命令                                 | 说明                |
| ---------------------------------- | ----------------- |
| `git remote -v`                    | 查看远程库信息           |
| `git remote show <remote>`         | 查看远程分支的信息         |
| `git remote add <shortname> <url>` | 建立本地仓库与远程仓库关联     |
| `git pull <remote> <branch>`       | 从远程拉取所有变化至本地并合并   |
| `git fetch <remote>`               | 从远程拉取所有变化至本地，但不合并 |
| `git push <remote> <branch>`       | 将本地的修改推送到远程       |
| `git push --tags`                  | 推送标签至远程           |

## 合并

| 命令                    | 说明          |
| --------------------- | ----------- |
| `git merge <branch>`  | 合并指定分支至当前分支 |
| `git rebase <branch>` |             |
|                       |             |

## 撤销

| 命令                       | 说明                               |
| ------------------------ | -------------------------------- |
| `git reset --hard HEAD`  | 丢弃对工作区的所有更改                      |
| `git checkout -- <file>` | 丢弃对本地文件的所有更改，让工作区的文件恢复到和暂存区相同的状态 |
|                          |                                  |
|                          |                                  |
|                          |                                  |
|                          |                                  |