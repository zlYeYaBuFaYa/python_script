#!/bin/bash

# Docker Engine 安装脚本 - 适用于Ubuntu系统
# 作者: Auto-generated
# 日期: 2025-11-19

set -e  # 遇到错误立即退出

echo "=========================================="
echo "开始安装 Docker Engine"
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

# 4. 添加Docker官方GPG密钥
echo ""
echo "[4/7] 添加 Docker 官方 GPG 密钥..."
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
chmod a+r /etc/apt/keyrings/docker.gpg

# 5. 设置Docker仓库
echo ""
echo "[5/7] 设置 Docker 仓库..."
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
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

echo ""
echo "=========================================="
echo "✅ Docker Engine 安装成功！"
echo "=========================================="
echo ""
echo "常用命令："
echo "  - 查看Docker版本: docker --version"
echo "  - 查看Docker状态: systemctl status docker"
echo "  - 查看运行的容器: docker ps"
echo "  - 查看所有容器: docker ps -a"
echo "  - 查看镜像: docker images"
echo ""
echo "如需将普通用户添加到docker组（免sudo）："
echo "  sudo usermod -aG docker \$USER"
echo "  然后重新登录系统使更改生效"
echo ""

