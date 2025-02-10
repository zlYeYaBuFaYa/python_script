## vscode 远程同步:

### 1. 文档连接: https://zhuanlan.zhihu.com/p/592665950

### 2. 配置文件实例:

```
{
    "name": "zlyybfy",
    "host": "127.0.0.1",
    "protocol": "sftp",
    "port": 22,
    "secure": true,
    "username": "root",
    "remotePath": "/home/zlyybfy/WorkSpace/djangoDemo",
    "password": "521877",
    "uploadOnSave": true,
    "ignore": [
        ".vscode",
        ".git",
        ".idea"
    ]
}
```

### 3. 插件: vscode->sftp

```
a. Ctrl+Shift+P 打开命令面板
b. SFTP:Config 命令后打开sftp.json文件，项目中自动新增.vscode目录，里面包含sftp.json模板文件
c. 修改name、host、port、username等信息，新的sftp.json
d. 配置完成并保存后在命令面板中输入>SFTP:Open SSH in Terminal以连接远端的服务器
f. 选择要连接的SFTP服务器
g. SFTP连接成功后，在左侧空白处右键选择“Sync Local->Remote”将代码同步到远程服务器，同步成功后本地修改或者删除代码时都会自动和远端服务器同步(因为在sftp.json中设置"uploadOnSave": true)。（建议先在远端新建项目路径，在sftp.json中设置该路径为remotePath，即指定了本地代码同步到远端的路径）
```
