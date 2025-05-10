## docker 容器

### 一. mongo:

- 1. 命令:

```
docker run -d --name my-mongo -p 27017:27017 --privileged=true --restart=always -v E:/mongodb/data:/data/db -v E:/mongodb/conf:/data/configdb -v E:/mongodb/logs:/data/log/ -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=123456 mongo -f /data/configdb/mongod.conf
```

### 二. mysql:

- 1. 命令:

```
# windows
docker run -d --name my-mysql -p 3306:3306 --privileged=true --restart=always -v E:/mysql/data:/var/lib/mysql -v E:/mysql/conf:/etc/mysql/conf.d -v E:/mysql/logs:/var/log/mysql -e MYSQL_ROOT_PASSWORD=123456 mysql

# mac
docker run -d --name my-mysql -p 3306:3306 --privileged=true --restart=always -v /Users/zlyybfy/docker/mysql/data:/var/lib/mysql -v /Users/zlyybfy/docker/mysql/conf:/etc/mysql/conf.d -v /Users/zlyybfy/docker/mysql/logs:/var/log/mysql -e MYSQL_ROOT_PASSWORD=123456 mysql
```
