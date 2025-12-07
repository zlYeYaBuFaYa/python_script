#!/bin/bash

# Node.js 自动安装脚本（使用阿里云镜像源）
# 支持 CentOS、Ubuntu、Debian 系统

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Node.js 版本（默认 20.x LTS）
NODE_VERSION="${1:-24}"

echo -e "${GREEN}=========================================="
echo "Node.js 自动安装脚本（阿里云镜像源）"
echo "==========================================${NC}"

# 检测系统类型
detect_os() {
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        OS=$ID
        OS_VERSION=$VERSION_ID
    elif type lsb_release >/dev/null 2>&1; then
        OS=$(lsb_release -si | tr '[:upper:]' '[:lower:]')
        OS_VERSION=$(lsb_release -sr)
    elif [ -f /etc/lsb-release ]; then
        . /etc/lsb-release
        OS=$DISTRIB_ID
        OS_VERSION=$DISTRIB_RELEASE
    elif [ -f /etc/debian_version ]; then
        OS=debian
        OS_VERSION=$(cat /etc/debian_version)
    elif [ -f /etc/redhat-release ]; then
        OS=rhel
        OS_VERSION=$(cat /etc/redhat-release | sed 's/.*release \([0-9.]*\).*/\1/')
    else
        echo -e "${RED}错误: 无法检测系统类型${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}检测到系统: $OS $OS_VERSION${NC}"
}

# 检查是否已安装 Node.js
check_node_installed() {
    if command -v node &> /dev/null; then
        CURRENT_VERSION=$(node -v | sed 's/v//')
        echo -e "${YELLOW}检测到已安装 Node.js 版本: v$CURRENT_VERSION${NC}"
        read -p "是否要重新安装？(y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo -e "${GREEN}跳过安装${NC}"
            exit 0
        fi
    fi
}

# 安装 Node.js（使用 nvm）
install_node_with_nvm() {
    echo -e "${GREEN}使用 NVM 安装 Node.js...${NC}"
    
    # 安装 nvm
    if [ ! -d "$HOME/.nvm" ]; then
        echo "正在安装 NVM..."
        curl -o- https://gitee.com/mirrors/nvm/raw/master/install.sh | bash
        
        # 加载 nvm
        export NVM_DIR="$HOME/.nvm"
        [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
        [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
    else
        echo "NVM 已安装，加载中..."
        export NVM_DIR="$HOME/.nvm"
        [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
        [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
    fi
    
    # 配置 nvm 使用淘宝镜像
    export NVM_NODEJS_ORG_MIRROR=https://npmmirror.com/mirrors/node/
    
    # 安装指定版本的 Node.js
    echo "正在安装 Node.js v$NODE_VERSION..."
    nvm install $NODE_VERSION
    nvm use $NODE_VERSION
    nvm alias default $NODE_VERSION
    
    # 验证安装
    if command -v node &> /dev/null; then
        INSTALLED_VERSION=$(node -v)
        echo -e "${GREEN}Node.js 安装成功: $INSTALLED_VERSION${NC}"
    else
        echo -e "${RED}Node.js 安装失败${NC}"
        exit 1
    fi
}

# 安装 Node.js（使用 NodeSource，适用于 Ubuntu/Debian）
install_node_ubuntu() {
    echo -e "${GREEN}使用 NodeSource 安装 Node.js（Ubuntu/Debian）...${NC}"
    
    # 更新系统
    sudo apt-get update
    
    # 安装必要的工具
    sudo apt-get install -y curl gnupg2 software-properties-common
    
    # 使用阿里云镜像的 NodeSource 仓库
    # 注意：这里使用官方 NodeSource，但配置 npm 使用国内镜像
    curl -fsSL https://deb.nodesource.com/setup_${NODE_VERSION}.x | sudo -E bash -
    
    # 安装 Node.js
    sudo apt-get install -y nodejs
    
    # 验证安装
    if command -v node &> /dev/null; then
        INSTALLED_VERSION=$(node -v)
        echo -e "${GREEN}Node.js 安装成功: $INSTALLED_VERSION${NC}"
    else
        echo -e "${RED}Node.js 安装失败${NC}"
        exit 1
    fi
}

# 安装 Node.js（使用 NodeSource，适用于 CentOS/RHEL）
install_node_centos() {
    echo -e "${GREEN}使用 NodeSource 安装 Node.js（CentOS/RHEL）...${NC}"
    
    # 安装必要的工具
    sudo yum install -y curl
    
    # 使用 NodeSource 仓库
    curl -fsSL https://rpm.nodesource.com/setup_${NODE_VERSION}.x | sudo bash -
    
    # 安装 Node.js
    sudo yum install -y nodejs
    
    # 验证安装
    if command -v node &> /dev/null; then
        INSTALLED_VERSION=$(node -v)
        echo -e "${GREEN}Node.js 安装成功: $INSTALLED_VERSION${NC}"
    else
        echo -e "${RED}Node.js 安装失败${NC}"
        exit 1
    fi
}

# 配置 npm 使用国内镜像
configure_npm_mirror() {
    echo -e "${GREEN}配置 npm 使用国内镜像源...${NC}"
    
    # 设置 npm 主镜像源（这是最重要的）
    npm config set registry https://registry.npmmirror.com
    
    # 设置环境变量（用于某些包的下载，兼容性更好）
    # 这些环境变量会被某些构建工具使用
    export ELECTRON_MIRROR=https://npmmirror.com/mirrors/electron/
    export SASS_BINARY_SITE=https://npmmirror.com/mirrors/node-sass/
    export PUPPETEER_DOWNLOAD_HOST=https://npmmirror.com/mirrors
    export CHROMEDRIVER_CDNURL=https://npmmirror.com/mirrors/chromedriver
    export OPERADRIVER_CDNURL=https://npmmirror.com/mirrors/operadriver
    export PHANTOMJS_CDNURL=https://npmmirror.com/mirrors/phantomjs
    export SELENIUM_CDNURL=https://npmmirror.com/mirrors/selenium
    export NODE_INSPECTOR_CDNURL=https://npmmirror.com/mirrors/node-inspector
    
    # 将这些环境变量写入 .npmrc（如果支持的话）
    # 注意：某些配置项在新版 npm 中已不支持，使用环境变量更可靠
    if npm config set electron_mirror https://npmmirror.com/mirrors/electron/ 2>/dev/null; then
        echo "已配置 electron_mirror"
    fi
    
    if npm config set sass_binary_site https://npmmirror.com/mirrors/node-sass/ 2>/dev/null; then
        echo "已配置 sass_binary_site"
    fi
    
    if npm config set puppeteer_download_host https://npmmirror.com/mirrors 2>/dev/null; then
        echo "已配置 puppeteer_download_host"
    fi
    
    if npm config set chromedriver_cdnurl https://npmmirror.com/mirrors/chromedriver 2>/dev/null; then
        echo "已配置 chromedriver_cdnurl"
    fi
    
    # 将环境变量写入 ~/.bashrc 和 ~/.zshrc，以便持久化
    NPM_ENV_CONFIG="
# npm 国内镜像环境变量配置
export ELECTRON_MIRROR=https://npmmirror.com/mirrors/electron/
export SASS_BINARY_SITE=https://npmmirror.com/mirrors/node-sass/
export PUPPETEER_DOWNLOAD_HOST=https://npmmirror.com/mirrors
export CHROMEDRIVER_CDNURL=https://npmmirror.com/mirrors/chromedriver
export OPERADRIVER_CDNURL=https://npmmirror.com/mirrors/operadriver
export PHANTOMJS_CDNURL=https://npmmirror.com/mirrors/phantomjs
export SELENIUM_CDNURL=https://npmmirror.com/mirrors/selenium
export NODE_INSPECTOR_CDNURL=https://npmmirror.com/mirrors/node-inspector
"
    
    # 添加到 .bashrc（如果存在且未添加）
    if [ -f ~/.bashrc ] && ! grep -q "ELECTRON_MIRROR" ~/.bashrc; then
        echo "$NPM_ENV_CONFIG" >> ~/.bashrc
        echo "已将环境变量配置添加到 ~/.bashrc"
    fi
    
    # 添加到 .zshrc（如果存在且未添加）
    if [ -f ~/.zshrc ] && ! grep -q "ELECTRON_MIRROR" ~/.zshrc; then
        echo "$NPM_ENV_CONFIG" >> ~/.zshrc
        echo "已将环境变量配置添加到 ~/.zshrc"
    fi
    
    echo -e "${GREEN}npm 镜像源配置完成${NC}"
    
    # 显示当前配置
    echo -e "${YELLOW}当前 npm 配置:${NC}"
    npm config get registry
}

# 安装常用全局包
install_global_packages() {
    echo -e "${GREEN}安装常用全局包...${NC}"
    
    # 安装 yarn（使用国内镜像）
    if ! command -v yarn &> /dev/null; then
        echo "正在安装 yarn..."
        npm install -g yarn --registry=https://registry.npmmirror.com
        yarn config set registry https://registry.npmmirror.com
    fi
    
    # 安装 pnpm（使用国内镜像）
    if ! command -v pnpm &> /dev/null; then
        echo "正在安装 pnpm..."
        npm install -g pnpm --registry=https://registry.npmmirror.com
        pnpm config set registry https://registry.npmmirror.com
    fi
    
    echo -e "${GREEN}全局包安装完成${NC}"
}

# 显示安装信息
show_info() {
    echo -e "${GREEN}=========================================="
    echo "安装完成！"
    echo "==========================================${NC}"
    echo -e "${YELLOW}Node.js 版本:${NC} $(node -v)"
    echo -e "${YELLOW}npm 版本:${NC} $(npm -v)"
    echo -e "${YELLOW}npm 镜像源:${NC} $(npm config get registry)"
    
    if command -v yarn &> /dev/null; then
        echo -e "${YELLOW}yarn 版本:${NC} $(yarn -v)"
    fi
    
    if command -v pnpm &> /dev/null; then
        echo -e "${YELLOW}pnpm 版本:${NC} $(pnpm -v)"
    fi
    
    echo -e "${GREEN}==========================================${NC}"
}

# 主函数
main() {
    # 检测系统
    detect_os
    
    # 检查是否已安装
    check_node_installed
    
    # 根据系统类型安装
    case $OS in
        ubuntu|debian)
            install_node_ubuntu
            ;;
        centos|rhel|fedora)
            install_node_centos
            ;;
        *)
            echo -e "${YELLOW}未识别的系统类型，尝试使用 NVM 安装...${NC}"
            install_node_with_nvm
            ;;
    esac
    
    # 配置 npm 镜像
    configure_npm_mirror
    
    # 安装全局包（可选）
    read -p "是否安装常用全局包（yarn、pnpm）？(Y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Nn]$ ]]; then
        install_global_packages
    fi
    
    # 显示安装信息
    show_info
}

# 运行主函数
main

