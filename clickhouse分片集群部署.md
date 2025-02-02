## clickhouse 分片集群部署

- 1. docker， docker-compose 安装

```
a. 配置2分片，2副本集群：
节点名称:
    clickhouse-shard1-replica1
    clickhouse-shard1-replica2
    clickhouse-shard2-replica1
    clickhouse-shard2-replica2
```

- 2. docker-compose.yml 文件

```
version: '3.7'

services:
  zookeeper:
    image: zookeeper:3.8
    container_name: zookeeper
    ports:
      - "2181:2181"
    networks:
      - clickhouse-net

  clickhouse-shard1-replica1:
    image: clickhouse/clickhouse-server
    container_name: clickhouse-shard1-replica1
    ports:
      - "9001:9000"
      - "8123:8123"
    volumes:
      - ./configs/shard1-replica1/config.xml:/etc/clickhouse-server/config.xml
      - ./configs/shard1-replica1/users.xml:/etc/clickhouse-server/users.xml
      - ./data/shard1-replica1:/var/lib/clickhouse
      - ./logs/shard1-replica1:/var/log/clickhouse-server
    networks:
      - clickhouse-net
    depends_on:
      - zookeeper

  clickhouse-shard1-replica2:
    image: clickhouse/clickhouse-server
    container_name: clickhouse-shard1-replica2
    ports:
      - "9002:9000"
      - "8124:8123"
    volumes:
      - ./configs/shard1-replica2/config.xml:/etc/clickhouse-server/config.xml
      - ./configs/shard1-replica2/users.xml:/etc/clickhouse-server/users.xml
      - ./data/shard1-replica2:/var/lib/clickhouse
      - ./logs/shard1-replica2:/var/log/clickhouse-server
    networks:
      - clickhouse-net
    depends_on:
      - zookeeper

  clickhouse-shard2-replica1:
    image: clickhouse/clickhouse-server
    container_name: clickhouse-shard2-replica1
    ports:
      - "9003:9000"
      - "8125:8123"
    volumes:
      - ./configs/shard2-replica1/config.xml:/etc/clickhouse-server/config.xml
      - ./configs/shard2-replica1/users.xml:/etc/clickhouse-server/users.xml
      - ./data/shard2-replica1:/var/lib/clickhouse
      - ./logs/shard2-replica1:/var/log/clickhouse-server
    networks:
      - clickhouse-net
    depends_on:
      - zookeeper

  clickhouse-shard2-replica2:
    image: clickhouse/clickhouse-server
    container_name: clickhouse-shard2-replica2
    ports:
      - "9004:9000"
      - "8126:8123"
    volumes:
      - ./configs/shard2-replica2/config.xml:/etc/clickhouse-server/config.xml
      - ./configs/shard2-replica2/users.xml:/etc/clickhouse-server/users.xml
      - ./data/shard2-replica2:/var/lib/clickhouse
      - ./logs/shard2-replica2:/var/log/clickhouse-server
    networks:
      - clickhouse-net
    depends_on:
      - zookeeper

networks:
  clickhouse-net:
    driver: bridge

```

- 3. docker-compose 命令：

```
1. docker-compose up -d 启动
2. docker-compose down -v 停止并删除 容器，network
```

- 4. 副本配置文件: config.yaml:

```
<yandex>
    <remote_servers>
        <cluster>
            <shard>
                <replica>
                    <host>clickhouse-shard1-replica1</host>
                    <port>9000</port>
                </replica>
                <replica>
                    <host>clickhouse-shard1-replica2</host>
                    <port>9000</port>
                </replica>
            </shard>
            <shard>
                <replica>
                    <host>clickhouse-shard2-replica1</host>
                    <port>9000</port>
                </replica>
                <replica>
                    <host>clickhouse-shard2-replica2</host>
                    <port>9000</port>
                </replica>
            </shard>
        </cluster>
    </remote_servers>

    <zookeeper>
        <node>
            <host>zookeeper</host>
            <port>2181</port>
        </node>
    </zookeeper>

    <macros>
        <shard>1</shard>
        <replica>replica1</replica>
    </macros>

    <listen_host>0.0.0.0</listen_host>
    <!-- TCP 端口 (用于客户端连接) -->
    <tcp_port>9000</tcp_port>

    <!-- HTTP 端口 (用于 HTTP API) -->
    <http_port>8123</http_port>

    <!-- 数据存储路径 -->
    <path>/var/lib/clickhouse/</path>

    <!-- 临时文件路径 -->
    <tmp_path>/var/lib/clickhouse/tmp/</tmp_path>

    <!-- 用户文件路径 -->
    <user_files_path>/var/lib/clickhouse/user_files/</user_files_path>

    <!-- 日志文件路径 -->
    <logger>
        <log>/var/log/clickhouse-server/clickhouse-server.log</log>
        <errorlog>/var/log/clickhouse-server/clickhouse-server.err.log</errorlog>
    </logger>

    <!-- 格式模式文件路径 -->
    <format_schema_path>/var/lib/clickhouse/format_schemas/</format_schema_path>
    <users_config>/etc/clickhouse-server/users.xml</users_config>
</yandex>
```

- 5. 副本用户配置文件: users.yaml

```
<yandex>
    <users>
        <default>
            <password></password>
            <networks>
                <ip>::/0</ip>
            </networks>
            <profile>default</profile>
            <quota>default</quota>
        </default>
    </users>

    <profiles>
        <default>
            <max_memory_usage>10000000000</max_memory_usage>
            <use_uncompressed_cache>0</use_uncompressed_cache>
            <load_balancing>random</load_balancing>
        </default>
    </profiles>

    <quotas>
        <default>
            <interval>
                <duration>3600</duration>
                <queries>0</queries>
                <errors>0</errors>
                <result_rows>0</result_rows>
                <read_rows>0</read_rows>
                <execution_time>0</execution_time>
            </interval>
        </default>
    </quotas>
</yandex>
```
