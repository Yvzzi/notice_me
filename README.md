# Notice Me

Notice your when you are using IBM Spectrum LSF.

## Get Started

1. 注册企业微信
2. 在[Server酱](https://sct.ftqq.com/)登录, 获取`SENDKEY`
3. 登录超算, 下载项目

```shell
git clone https://github.com/Yvzzi/notice_me
```

或者手动下载 https://github.com/Yvzzi/notice_me/archive/refs/heads/main.zip

1. 配置 `SENDKEY` 和启动服务

```shell
cd path/to/notice_me # 切换到notice_me目录
chmod +x notice_me.sh # 添加可执行权限
./notice_me.sh set-sendkey
./notice_me.sh on
```

5. 关闭服务

```shell
cd path/to/notice_me # 切换到notice_me目录
./notice_me.sh off
```

6. 更新

更新前先确保已经关闭服务
```shell
cd path/to/notice_me # 切换到notice_me目录
./notice_me.sh off
```

然后切换到上级目录

```shell
cd path/to/notice_me/.. # 切换到notice_me上级目录
```

然后下载

```shell
git clone https://github.com/Yvzzi/notice_me
```

或者手动下载 https://github.com/Yvzzi/notice_me/archive/refs/heads/main.zip