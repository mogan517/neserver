<!--
 * @Author: 侯成
 * @Email: cheng.hou@chinatalentgroup.com
 * @since: 2019-07-29 09:38:29
 * @lastTime: 2019-09-04 14:32:07
 * @LastAuthor: Do not edit
 * @message: 
 -->

<h1 align="center">Candy HRO 新前端</h1>

<div align="center">

An out-of-box UI solution for enterprise applications as a React boilerplate.
</div>
# 相关文档

## 环境搭建

### Git相关操作

 * 配置`ssh`公钥
 `id_rsa_username` 为公钥文件名，因人而异。
 ```sh
 mv id_rsa_username ~/.ssh\
 ```
 * 配置`ssh config` 
 `username` 为计算机当前用户名

  ```sh
  # 编辑 ~/.ssh/config
  Host chro
        Hostname 192.168.101.8
        User houcer
        IdentityFile "/c/Users/username/.ssh/id_rsa_username"
        IdentitiesOnly yes
  ```
 * 拉取代码
 ```sh
  git clone git@192.168.101.8:chro_web

  # 进入项目文件夹
  cd chro_web
 ```

 * 本地切换至`dev`分支，并追踪远程`dev`分支
 ```sh
  git checkout -b dev origin/dev
 ```
 *  **最后**，在本地新建新分支 `ayanami` (名称随意)并切入，防手贱专用，仅在此分支上倒腾代码，不必追踪远程库。
 ```sh
  git branch ayanami
 ```

### Git开发流程

####  开发工作在本地`ayanami`分支进行
经常`commit`是好习惯，设置游戏缓存点，防作死。

#### 游戏缓存点
一个或多个组件开发完毕后，通常还处于半成品状态，按需缓存存档。

 * 操作之前先查看分支情况，也是极好的。 命令及输出。
 ```sh
  git status
        modified:   README.md
 ```
 * 查看所在分支

 ```sh
  git branch
        dev
      * ayanami
        master
 ```

 * `git`添加所有新文件

 ```sh
  git add .
  git commit -m "这里写本次提交的内容说明"
 ```

 ####  阶段性缓存点
 通常在一个公共组件、完整页面、完整业务逻辑开发完成后，进行阶段存档。简单说就是，代码要提交给别人用了。
 * 在 `ayanami` 分支 `add` 并 `commit` 之后，推送至远程仓库，随后合并 `dev`分支
 ```sh
  git push
 ```
 第一次push时会报错，提示没有追踪远程库的`ayanami`分支
 ```sh
  git checkout -b ayanami origin/ayanami
 ```
远程库中的`ayanami`分支，属于个人私有，仅有自己追踪，各不影响。
推送成功后，切换回`dev`分支。
 ```sh
  git checkout dev
 ```
 * 查看所在分支
 ```sh
  git branch
    * dev
      ayanami
      master
 ```
 * 拉取远程`dev`分支
 ```sh
  git pull
 ```
 * 合并之前的所有阶段性代码至dev分支
 ```sh
  git merge ayanami
 ```
合并个人分支时时可能会有冲突，需进行相关处理。
* 推送至远程仓库
 ```sh
  # 推送到远程库，送孩子出嫁。
  git push
 ```
 * 切换回个人分支并合并dev中的更改。
 ```sh
  git checkout ayanami
  git merge dev
 ```
 #### 开始下一阶段
 * 开始下一轮开发

 ### 开发文档
 1.1 安装`gitbook-cli`工具

 `Linux`及`Mac`
 ```sh
sduo yarn global add gitbook-cli

gitbook --version
```
`windos`
```sh
yarn global add gitbook-cli

gitbook --version
```
 1.2 安装`gitbook`插件
 ```sh
 cd doc
 gitbook install
 ```

 #### END

### Appendix
clone 特定分支
```sh
git clone --single-branch --branch v4 https://github.com/ant-design/ant-design-pro.git
```
