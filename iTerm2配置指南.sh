#!/bin/bash

# iTerm2 美化配置脚本
# 包含：Oh My Zsh + Powerlevel10k + Solarized Dark 配色
# 作者: Auto-generated
# 日期: 2025-11-19

set -e

# echo "=========================================="
# echo "iTerm2 美化配置脚本"
# echo "=========================================="
# echo ""
# echo "将会安装："
# echo "  1. Oh My Zsh - Zsh 配置管理框架"
# echo "  2. Powerlevel10k - 强大的主题"
# echo "  3. zsh-autosuggestions - 自动补全插件"
# echo "  4. zsh-syntax-highlighting - 语法高亮插件"
# echo ""

# # 检查是否安装了 Homebrew
# if ! command -v brew &> /dev/null; then
#     echo "未检测到 Homebrew，正在安装..."
#     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# else
#     echo "✓ Homebrew 已安装"
# fi

# # 1. 安装 Oh My Zsh
# echo ""
# echo "[1/4] 安装 Oh My Zsh..."
# if [ -d "$HOME/.oh-my-zsh" ]; then
#     echo "✓ Oh My Zsh 已安装，跳过"
# else
#     sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
#     echo "✓ Oh My Zsh 安装完成"
# fi

# # 2. 安装 Powerlevel10k
# echo ""
# echo "[2/4] 安装 Powerlevel10k 主题..."
# if [ -d "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k" ]; then
#     echo "✓ Powerlevel10k 已安装，更新中..."
#     git -C "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k" pull
# else
#     git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
#     echo "✓ Powerlevel10k 安装完成"
# fi

# # 3. 安装推荐字体
# echo ""
# echo "[3/4] 安装 Nerd Fonts（Powerlevel10k 需要）..."
# brew tap homebrew/cask-fonts 2>/dev/null || true
# brew install --cask font-meslo-lg-nerd-font 2>/dev/null || echo "✓ 字体已安装"

# 4. 安装推荐插件
# echo ""
# echo "[4/4] 安装推荐插件..."

# # zsh-autosuggestions
# if [ -d "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-autosuggestions" ]; then
#     echo "✓ zsh-autosuggestions 已安装"
# else
#     git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
#     echo "✓ zsh-autosuggestions 安装完成"
# fi

# # zsh-syntax-highlighting
# if [ -d "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting" ]; then
#     echo "✓ zsh-syntax-highlighting 已安装"
# else
#     git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
#     echo "✓ zsh-syntax-highlighting 安装完成"
# fi

# 5. 配置 .zshrc
echo ""
echo "配置 .zshrc 文件..."
cp ~/.zshrc ~/.zshrc.backup.$(date +%Y%m%d%H%M%S) 2>/dev/null || true

# 更新主题
sed -i '' 's/^ZSH_THEME=.*/ZSH_THEME="powerlevel10k\/powerlevel10k"/' ~/.zshrc

# 更新插件
if grep -q "^plugins=" ~/.zshrc; then
    sed -i '' 's/^plugins=.*/plugins=(git docker kubectl zsh-autosuggestions zsh-syntax-highlighting)/' ~/.zshrc
else
    echo 'plugins=(git docker kubectl zsh-autosuggestions zsh-syntax-highlighting)' >> ~/.zshrc
fi

echo ""
echo "=========================================="
echo "✅ 安装完成！"
echo "=========================================="
echo ""
echo "下一步："
echo ""
echo "1. 重启终端或运行："
echo "   source ~/.zshrc"
echo ""
echo "2. 首次启动会进入 Powerlevel10k 配置向导"
echo "   按照提示选择你喜欢的样式即可"
echo ""
echo "3. 如需重新配置主题，运行："
echo "   p10k configure"
echo ""
echo "4. 在 iTerm2 中设置配色方案为 Solarized Dark："
echo "   - 打开 iTerm2 → Preferences (⌘,)"
echo "   - Profiles → Colors"
echo "   - Color Presets → Solarized Dark"
echo ""
echo "5. 设置字体："
echo "   - Profiles → Text"
echo "   - Font → MesloLGS NF (14pt)"
echo ""

