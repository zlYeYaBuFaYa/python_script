#!/bin/bash

# Ubuntu 系统 Oh My Zsh + Powerlevel10k 安装脚本
# 适用于阿里云 Ubuntu 服务器
# 作者: Auto-generated
# 日期: 2025-11-19

set -e

echo "=========================================="
echo "Ubuntu 系统 Oh My Zsh 美化脚本"
echo "=========================================="
echo ""
echo "将会安装："
echo "  1. Zsh - 强大的Shell"
echo "  2. Oh My Zsh - Zsh 配置管理框架"
echo "  3. Powerlevel10k - 强大的主题"
echo "  4. zsh-autosuggestions - 自动补全插件"
echo "  5. zsh-syntax-highlighting - 语法高亮插件"
echo ""

# 检查是否为root用户或使用sudo
if [ "$EUID" -ne 0 ]; then 
    SUDO='sudo'
    echo "将使用 sudo 权限安装"
else
    SUDO=''
    echo "使用 root 权限安装"
fi

# 1. 更新系统并安装依赖
echo ""
echo "[1/6] 更新系统并安装依赖..."
$SUDO apt-get update
$SUDO apt-get install -y git curl wget zsh

# 2. 将 zsh 设置为默认 shell
echo ""
echo "[2/6] 设置 zsh 为默认 shell..."
if [ "$SHELL" != "$(which zsh)" ]; then
    echo "当前 shell: $SHELL"
    echo "切换到 zsh..."
    chsh -s $(which zsh)
    echo "✓ 默认 shell 已设置为 zsh（需要重新登录生效）"
else
    echo "✓ zsh 已经是默认 shell"
fi

# 3. 安装 Oh My Zsh
echo ""
echo "[3/6] 安装 Oh My Zsh..."
if [ -d "$HOME/.oh-my-zsh" ]; then
    echo "✓ Oh My Zsh 已安装，跳过"
else
    # 使用国内镜像加速（可选）
    # export REMOTE=https://gitee.com/mirrors/oh-my-zsh.git
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
    echo "✓ Oh My Zsh 安装完成"
fi

# 4. 安装 Powerlevel10k 主题
echo ""
echo "[4/6] 安装 Powerlevel10k 主题..."
if [ -d "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k" ]; then
    echo "✓ Powerlevel10k 已安装，更新中..."
    git -C "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k" pull
else
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
    echo "✓ Powerlevel10k 安装完成"
fi

# 5. 安装推荐插件
echo ""
echo "[5/6] 安装推荐插件..."

# zsh-autosuggestions
if [ -d "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-autosuggestions" ]; then
    echo "✓ zsh-autosuggestions 已安装"
else
    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
    echo "✓ zsh-autosuggestions 安装完成"
fi

# zsh-syntax-highlighting
if [ -d "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting" ]; then
    echo "✓ zsh-syntax-highlighting 已安装"
else
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
    echo "✓ zsh-syntax-highlighting 安装完成"
fi

# 6. 配置 .zshrc
echo ""
echo "[6/6] 配置 .zshrc 文件..."

# 备份原配置
if [ -f ~/.zshrc ]; then
    cp ~/.zshrc ~/.zshrc.backup.$(date +%Y%m%d%H%M%S)
    echo "✓ 已备份原 .zshrc 文件"
fi

# 更新主题
sed -i 's/^ZSH_THEME=.*/ZSH_THEME="powerlevel10k\/powerlevel10k"/' ~/.zshrc

# 更新插件
if grep -q "^plugins=" ~/.zshrc; then
    sed -i 's/^plugins=.*/plugins=(git docker kubectl zsh-autosuggestions zsh-syntax-highlighting)/' ~/.zshrc
else
    echo 'plugins=(git docker kubectl zsh-autosuggestions zsh-syntax-highlighting)' >> ~/.zshrc
fi

# 启用自动更新
if ! grep -q "zstyle ':omz:update' mode auto" ~/.zshrc; then
    sed -i "s/# zstyle ':omz:update' mode auto/zstyle ':omz:update' mode auto/" ~/.zshrc
fi

echo "✓ .zshrc 配置完成"

echo ""
echo "=========================================="
echo "✅ 安装完成！"
echo "=========================================="
echo ""
echo "下一步："
echo ""
echo "1. 重新登录 SSH 使 zsh 成为默认 shell"
echo "   exit"
echo "   ssh user@your_server_ip"
echo ""
echo "2. 或者立即切换到 zsh："
echo "   zsh"
echo ""
echo "3. 首次启动会进入 Powerlevel10k 配置向导"
echo "   按照提示选择你喜欢的样式"
echo ""
echo "4. 如需重新配置主题，运行："
echo "   p10k configure"
echo ""
echo "5. 常用命令："
echo "   - 更新 Oh My Zsh: omz update"
echo "   - 查看所有插件: ls ~/.oh-my-zsh/plugins/"
echo "   - 编辑配置: nano ~/.zshrc"
echo "   - 重新加载配置: source ~/.zshrc"
echo ""
echo "📝 注意："
echo "   - 如果是通过 SSH 连接，建议使用支持 Nerd Font 的终端"
echo "   - macOS 推荐使用 iTerm2"
echo "   - Windows 推荐使用 Windows Terminal 或 MobaXterm"
echo ""

