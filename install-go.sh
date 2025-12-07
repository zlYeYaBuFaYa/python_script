#!/bin/bash

# Ubuntu 自动安装 Go 1.21 脚本
# 包含国内代理配置

set -e

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Go 版本
GO_VERSION="1.21.6"
GO_ARCH="amd64"
GO_OS="linux"

# 安装目录
GO_INSTALL_DIR="/usr/local"
GO_ROOT="$GO_INSTALL_DIR/go"
GO_PATH="$HOME/go"

# 国内代理配置
GOPROXY_CN="https://goproxy.cn,direct"
GOSUMDB="sum.golang.google.cn"

echo "=========================================="
echo "Ubuntu Go 1.21 自动安装脚本"
echo "=========================================="

# 检查是否为 root 用户
if [ "$EUID" -ne 0 ]; then 
    echo -e "${RED}错误: 请使用 sudo 运行此脚本${NC}"
    exit 1
fi

# 检查系统类型
if [ ! -f /etc/os-release ]; then
    echo -e "${RED}错误: 无法检测系统类型${NC}"
    exit 1
fi

. /etc/os-release

if [ "$ID" != "ubuntu" ] && [ "$ID" != "debian" ]; then
    echo -e "${YELLOW}警告: 此脚本专为 Ubuntu/Debian 设计，当前系统: $ID${NC}"
    read -p "是否继续? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

echo -e "${GREEN}系统信息: $PRETTY_NAME${NC}"

# 检查是否已安装 Go
if command -v go &> /dev/null; then
    CURRENT_VERSION=$(go version | awk '{print $3}' | sed 's/go//')
    echo -e "${YELLOW}检测到已安装 Go 版本: $CURRENT_VERSION${NC}"
    read -p "是否卸载旧版本并安装 Go $GO_VERSION? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "安装已取消"
        exit 0
    fi
    
    # 卸载旧版本
    echo "正在卸载旧版本..."
    rm -rf $GO_ROOT
    rm -rf $GO_PATH
    # 从 PATH 中移除（需要用户手动处理 ~/.bashrc 或 ~/.zshrc）
fi

# 创建临时目录
TMP_DIR=$(mktemp -d)
cd $TMP_DIR

echo "=========================================="
echo "步骤 1: 下载 Go $GO_VERSION"
echo "=========================================="

GO_TARBALL="go${GO_VERSION}.${GO_OS}-${GO_ARCH}.tar.gz"
GO_DOWNLOAD_URL="https://golang.google.cn/dl/${GO_TARBALL}"

echo "下载地址: $GO_DOWNLOAD_URL"
echo "正在下载..."

# 下载 Go（使用国内镜像）
if ! wget -q --show-progress "$GO_DOWNLOAD_URL" -O "$GO_TARBALL"; then
    echo -e "${RED}错误: 下载失败，尝试备用地址...${NC}"
    # 备用地址
    GO_DOWNLOAD_URL="https://dl.google.com/go/${GO_TARBALL}"
    if ! wget -q --show-progress "$GO_DOWNLOAD_URL" -O "$GO_TARBALL"; then
        echo -e "${RED}错误: 下载失败，请检查网络连接${NC}"
        exit 1
    fi
fi

echo -e "${GREEN}下载完成${NC}"

# 验证下载文件
if [ ! -f "$GO_TARBALL" ]; then
    echo -e "${RED}错误: 下载文件不存在${NC}"
    exit 1
fi

echo "=========================================="
echo "步骤 2: 安装 Go"
echo "=========================================="

# 删除旧版本（如果存在）
if [ -d "$GO_ROOT" ]; then
    echo "删除旧版本..."
    rm -rf $GO_ROOT
fi

# 解压到安装目录
echo "正在解压..."
tar -C $GO_INSTALL_DIR -xzf "$GO_TARBALL"

if [ ! -d "$GO_ROOT" ]; then
    echo -e "${RED}错误: 安装失败${NC}"
    exit 1
fi

echo -e "${GREEN}安装完成${NC}"

echo "=========================================="
echo "步骤 3: 配置环境变量"
echo "=========================================="

# 检测用户的 shell
USER_SHELL=$(getent passwd $SUDO_USER | cut -d: -f7)
SHELL_RC=""

if [[ "$USER_SHELL" == *"zsh"* ]]; then
    SHELL_RC="$HOME/.zshrc"
elif [[ "$USER_SHELL" == *"bash"* ]]; then
    SHELL_RC="$HOME/.bashrc"
else
    SHELL_RC="$HOME/.profile"
fi

# 如果文件不存在，创建它
if [ ! -f "$SHELL_RC" ]; then
    touch "$SHELL_RC"
fi

# 检查是否已配置
if grep -q "GOROOT" "$SHELL_RC"; then
    echo -e "${YELLOW}检测到已有 Go 配置，正在更新...${NC}"
    # 删除旧的 Go 配置
    sed -i '/# Go environment variables/,/^$/d' "$SHELL_RC"
fi

# 添加 Go 环境变量配置
cat >> "$SHELL_RC" << EOF

# Go environment variables
export GOROOT=$GO_ROOT
export GOPATH=$GO_PATH
export PATH=\$PATH:\$GOROOT/bin:\$GOPATH/bin

# Go 国内代理配置
export GOPROXY=$GOPROXY_CN
export GOSUMDB=$GOSUMDB
export GO111MODULE=on
EOF

# 立即生效（当前会话）
export GOROOT=$GO_ROOT
export GOPATH=$GO_PATH
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin
export GOPROXY=$GOPROXY_CN
export GOSUMDB=$GOSUMDB
export GO111MODULE=on

echo -e "${GREEN}环境变量已配置到: $SHELL_RC${NC}"

echo "=========================================="
echo "步骤 4: 创建 GOPATH 目录"
echo "=========================================="

# 创建 GOPATH 目录结构
mkdir -p $GO_PATH/{bin,pkg,src}
chown -R $SUDO_USER:$SUDO_USER $GO_PATH

echo -e "${GREEN}GOPATH 目录已创建: $GO_PATH${NC}"

echo "=========================================="
echo "步骤 5: 验证安装"
echo "=========================================="

# 验证 Go 安装
if command -v go &> /dev/null; then
    GO_VER=$(go version)
    echo -e "${GREEN}Go 安装成功!${NC}"
    echo "版本信息: $GO_VER"
    echo ""
    echo "环境变量:"
    echo "  GOROOT: $GOROOT"
    echo "  GOPATH: $GOPATH"
    echo "  GOPROXY: $GOPROXY"
    echo "  GOSUMDB: $GOSUMDB"
    echo ""
    echo "测试 Go 环境..."
    go env | grep -E "GOROOT|GOPATH|GOPROXY|GOSUMDB"
else
    echo -e "${RED}错误: Go 未正确安装${NC}"
    exit 1
fi

# 清理临时文件
cd /
rm -rf $TMP_DIR

echo "=========================================="
echo -e "${GREEN}安装完成!${NC}"
echo "=========================================="
echo ""
echo "重要提示:"
echo "1. 请运行以下命令使环境变量生效（或重新登录）:"
echo "   source $SHELL_RC"
echo ""
echo "2. 验证安装:"
echo "   go version"
echo "   go env GOPROXY"
echo ""
echo "3. 测试代理（可选）:"
echo "   go env -w GOPROXY=$GOPROXY_CN"
echo "   go env -w GOSUMDB=$GOSUMDB"
echo ""
echo "4. 如果使用 zsh，请确保 ~/.zshrc 已加载"
echo ""

