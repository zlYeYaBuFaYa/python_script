## docker 容器

### 一. mongo:

- 1. 命令:

```
docker run -d --name my-mongo -p 27017:27017 --privileged=true --restart=always -v E:/mongodb/data:/data/db -v E:/mongodb/conf:/data/configdb -v E:/mongodb/logs:/data/log/ -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=123456 mongo -f /data/configdb/mongod.conf
```
