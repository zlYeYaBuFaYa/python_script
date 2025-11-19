#!/bin/bash

# Docker Engine 安装脚本 - 适用于阿里云Ubuntu系统（使用阿里云镜像源）
# 作者: Auto-generated
# 日期: 2025-11-19

set -e  # 遇到错误立即退出

echo "=========================================="
echo "开始安装 Docker Engine (阿里云优化版)"
echo "=========================================="

# 检查是否为root用户
if [ "$EUID" -ne 0 ]; then 
    echo "请使用 root 权限运行此脚本"
    echo "使用命令: sudo bash $0"
    exit 1
fi

# 1. 更新apt包索引
echo ""
echo "[1/7] 更新 apt 包索引..."
apt-get update

# 2. 安装必要的依赖包
echo ""
echo "[2/7] 安装必要的依赖包..."
apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# 3. 创建keyrings目录
echo ""
echo "[3/7] 创建 keyrings 目录..."
mkdir -p /etc/apt/keyrings

# 4. 添加Docker官方GPG密钥（使用阿里云镜像）
echo ""
echo "[4/7] 添加 Docker 官方 GPG 密钥（阿里云镜像）..."
curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
chmod a+r /etc/apt/keyrings/docker.gpg

# 5. 设置Docker仓库（使用阿里云镜像）
echo ""
echo "[5/7] 设置 Docker 仓库（阿里云镜像）..."
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://mirrors.aliyun.com/docker-ce/linux/ubuntu \
  $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

# 6. 更新apt包索引并安装Docker Engine
echo ""
echo "[6/7] 安装 Docker Engine..."
apt-get update
apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# 7. 启动Docker服务
echo ""
echo "[7/7] 启动 Docker 服务..."
systemctl start docker
systemctl enable docker

# 配置Docker镜像加速器（阿里云）
echo ""
echo "配置 Docker 镜像加速器..."
mkdir -p /etc/docker
cat > /etc/docker/daemon.json <<EOF
{
  "registry-mirrors": [
    "https://p7ihrpmd.mirror.aliyuncs.com",
    "https://docker.mirrors.ustc.edu.cn",
    "https://hub-mirror.c.163.com",
    "https://mirror.ccs.tencentyun.com"
  ],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m",
    "max-file": "3"
  },
  "storage-driver": "overlay2"
}
EOF

# 重启Docker服务使配置生效
systemctl daemon-reload
systemctl restart docker

# 验证安装
echo ""
echo "=========================================="
echo "验证 Docker 安装..."
echo "=========================================="
docker --version
docker compose version

# 运行测试容器
echo ""
echo "运行 hello-world 测试容器..."
docker run --rm hello-world

# 显示Docker信息
echo ""
echo "Docker 系统信息："
docker info | grep -A 5 "Registry Mirrors"

echo ""
echo "=========================================="
echo "✅ Docker Engine 安装成功！"
echo "=========================================="
echo ""
echo "✨ 已配置国内镜像加速器，拉取镜像速度更快"
echo ""
echo "常用命令："
echo "  - 查看Docker版本: docker --version"
echo "  - 查看Docker状态: systemctl status docker"
echo "  - 查看运行的容器: docker ps"
echo "  - 查看所有容器: docker ps -a"
echo "  - 查看镜像: docker images"
echo "  - 拉取镜像: docker pull 镜像名"
echo ""
echo "如需将普通用户添加到docker组（免sudo）："
echo "  sudo usermod -aG docker \$USER"
echo "  然后重新登录系统使更改生效"
echo ""
echo "注意："
echo "  - 如果你有阿里云容器镜像服务账号，可以使用专属加速地址"
echo "  - 访问 https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors"
echo "  - 获取专属加速地址并替换 /etc/docker/daemon.json 中的配置"
echo ""

