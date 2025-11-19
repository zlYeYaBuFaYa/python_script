# iTerm2 美化配置完整教程

## 🎨 最终效果

完成后你将拥有：
- ✨ 漂亮的 Powerlevel10k 主题
- 🎨 Solarized Dark 配色方案
- ⚡ 智能命令补全
- 🌈 语法高亮
- 📊 Git 状态显示
- ⏱️ 命令执行时间显示

---

## 🚀 快速安装（推荐）

我已经为你准备好了一键安装脚本！

```bash
# 在本地终端运行（不是服务器！）
cd /Users/zlyybfy/workspace/python/python_script
chmod +x iTerm2配置指南.sh
./iTerm2配置指南.sh
```

安装完成后跳到 **[配置iTerm2配色](#配置iterm2配色方案)** 部分。

---

## 📝 手动安装步骤

如果你想了解每一步在做什么，可以按照下面的步骤手动配置。

### 步骤1️⃣：安装 Homebrew（如果还没有）

```bash
# 检查是否已安装
brew --version

# 如果没有，安装 Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 步骤2️⃣：安装 Oh My Zsh

```bash
# 安装 Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

安装完成后，你的默认 shell 会切换到 zsh。

### 步骤3️⃣：安装 Powerlevel10k 主题

```bash
# 克隆 Powerlevel10k 到 Oh My Zsh 主题目录
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

### 步骤4️⃣：安装推荐字体

Powerlevel10k 需要特殊字体来显示图标和符号。

```bash
# 安装字体
brew tap homebrew/cask-fonts
brew install --cask font-meslo-lg-nerd-font
```

### 步骤5️⃣：安装有用的插件

```bash
# 自动建议插件（根据历史记录自动补全）
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# 语法高亮插件
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

### 步骤6️⃣：配置 .zshrc

```bash
# 备份原配置
cp ~/.zshrc ~/.zshrc.backup

# 编辑配置文件
nano ~/.zshrc
```

**修改以下内容：**

1. **修改主题** - 找到 `ZSH_THEME` 这行，改为：
```bash
ZSH_THEME="powerlevel10k/powerlevel10k"
```

2. **启用插件** - 找到 `plugins` 这行，改为：
```bash
plugins=(
  git
  docker
  kubectl
  zsh-autosuggestions
  zsh-syntax-highlighting
)
```

保存并退出（`Ctrl + X`，然后 `Y`，回车）。

### 步骤7️⃣：应用配置

```bash
# 重新加载配置
source ~/.zshrc
```

第一次运行时，会自动启动 **Powerlevel10k 配置向导**。

---

## 🎨 Powerlevel10k 配置向导

运行 `source ~/.zshrc` 后，会出现配置向导，按照提示选择：

### 推荐选项：

1. **Diamond (菱形)** → `y`（显示正常则选y）
2. **Lock** → `y`
3. **Debian logo** → `y`
4. **Style** → `3` (Rainbow)
5. **Character Set** → `1` (Unicode)
6. **Show current time** → `2` (24-hour format)
7. **Prompt Separators** → `1` (Angled)
8. **Prompt Heads** → `1` (Sharp)
9. **Prompt Tails** → `1` (Flat)
10. **Prompt Height** → `2` (Two lines)
11. **Prompt Connection** → `2` (Dotted)
12. **Prompt Frame** → `2` (Left)
13. **Connection Color** → `1` (Lightest)
14. **Prompt Spacing** → `2` (Sparse)
15. **Icons** → `2` (Many icons)
16. **Prompt Flow** → `1` (Concise)
17. **Enable Transient Prompt** → `y`
18. **Instant Prompt Mode** → `1` (Verbose)

配置完成后，主题就生效了！

### 重新配置

如果想重新配置，随时运行：

```bash
p10k configure
```

---

## 🎨 配置iTerm2配色方案

### 方法一：使用内置配色（推荐）

1. **打开 iTerm2 偏好设置**
   - 快捷键：`⌘,` (Command + 逗号)
   - 或菜单：iTerm2 → Preferences

2. **设置配色**
   - 点击 `Profiles` 标签
   - 选择 `Colors` 子标签
   - 点击右下角 `Color Presets...` 下拉菜单
   - 选择 `Solarized Dark`

3. **设置字体**
   - 在 `Profiles` 中选择 `Text` 子标签
   - 点击 `Font` 下的 `Change Font`
   - 选择 `MesloLGS NF`（或 MesloLGS Nerd Font）
   - 字体大小推荐 `14` 或 `16`
   - ✅ 勾选 `Use ligatures`（如果有）

4. **其他推荐设置**
   - `Window` 标签 → 调整透明度（Transparency）为 10-20%（可选）
   - `Window` 标签 → 启用 `Blur`（可选，让背景模糊更好看）

### 方法二：导入更多配色方案

如果内置的 Solarized Dark 不够，可以导入更多配色：

```bash
# 克隆配色方案仓库
cd ~/Downloads
git clone https://github.com/mbadolato/iTerm2-Color-Schemes.git

# 导入所有配色
cd iTerm2-Color-Schemes/schemes
open .
```

然后在 iTerm2 中：
1. `Preferences` → `Profiles` → `Colors`
2. `Color Presets...` → `Import...`
3. 选择你喜欢的 `.itermcolors` 文件
4. 导入后在 `Color Presets...` 中选择即可

**推荐配色方案：**
- Solarized Dark（经典）
- Dracula（紫色系，护眼）
- Gruvbox Dark（复古风）
- Nord（冷色调）
- One Dark（类似 VSCode）

---

## ⚙️ 更多实用配置

### 配置快捷键

#### 设置热键窗口（一键呼出/隐藏终端）

1. `Preferences` → `Keys` → `Hotkey`
2. ✅ 勾选 `Create a Dedicated Hotkey Window`
3. 点击 `Configure Hotkey Window`
4. 设置快捷键，推荐：`⌥Space`（Option + 空格）
5. 完成！现在随时按快捷键即可呼出/隐藏终端

#### 分屏快捷键

iTerm2 默认分屏快捷键：
- `⌘D` - 垂直分屏（左右分割）
- `⌘⇧D` - 水平分屏（上下分割）
- `⌘⌥方向键` - 在分屏间切换
- `⌘⇧Enter` - 最大化当前分屏
- `⌘W` - 关闭当前分屏

### 启用自然文本编辑

让 iTerm2 支持常见的文本编辑快捷键：

1. `Preferences` → `Profiles` → `Keys`
2. 点击 `Key Mappings` 下的 `Presets...`
3. 选择 `Natural Text Editing`

现在可以使用：
- `⌥←` / `⌥→` - 按单词移动
- `⌘←` / `⌘→` - 移动到行首/行尾
- `⌘⌫` - 删除整行

---

## 🎯 .zshrc 完整配置示例

完整的 `~/.zshrc` 配置示例：

```bash
# Oh My Zsh 配置
export ZSH="$HOME/.oh-my-zsh"

# 主题
ZSH_THEME="powerlevel10k/powerlevel10k"

# 插件
plugins=(
  git
  docker
  kubectl
  brew
  macos
  colored-man-pages
  zsh-autosuggestions
  zsh-syntax-highlighting
)

source $ZSH/oh-my-zsh.sh

# Powerlevel10k 配置（由配置向导生成）
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

# 自定义别名
alias ll='ls -lah'
alias gs='git status'
alias gp='git pull'
alias dc='docker-compose'
alias k='kubectl'

# 自动建议插件配置
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=240'

# 历史记录配置
HISTSIZE=10000
SAVEHIST=10000
```

---

## 🐛 常见问题

### 1. 字体显示不正常，出现乱码或方框

**解决方法：**
- 确保安装了 Nerd Font
- 在 iTerm2 中设置正确的字体（MesloLGS NF）
- 重启 iTerm2

### 2. 配色不生效

**解决方法：**
- 确保在正确的 Profile 中设置（Default profile）
- 检查是否有其他配置覆盖了颜色设置

### 3. 插件不生效

**解决方法：**
```bash
# 检查插件是否正确安装
ls -la ~/.oh-my-zsh/custom/plugins/

# 确保 .zshrc 中插件名称正确
cat ~/.zshrc | grep plugins

# 重新加载配置
source ~/.zshrc
```

### 4. 想恢复到原来的配置

**解决方法：**
```bash
# 恢复备份
cp ~/.zshrc.backup ~/.zshrc

# 或者卸载 Oh My Zsh
uninstall_oh_my_zsh
```

---

## 📚 有用的命令

```bash
# 重新配置 Powerlevel10k
p10k configure

# 更新 Oh My Zsh
omz update

# 查看所有可用插件
ls ~/.oh-my-zsh/plugins/

# 查看所有可用主题
ls ~/.oh-my-zsh/themes/

# 编辑配置文件
nano ~/.zshrc

# 重新加载配置
source ~/.zshrc
```

---

## 🎉 完成！

现在你的 iTerm2 应该已经变得既强大又漂亮了！

### 配置效果：
- ✅ Powerlevel10k 主题
- ✅ Solarized Dark 配色
- ✅ 自动命令补全
- ✅ 语法高亮
- ✅ Git 状态显示
- ✅ 命令执行时间
- ✅ 美观的图标

享受你的新终端吧！🚀

---

## 💡 更多资源

- [Powerlevel10k GitHub](https://github.com/romkatv/powerlevel10k)
- [Oh My Zsh GitHub](https://github.com/ohmyzsh/ohmyzsh)
- [iTerm2 官网](https://iterm2.com)
- [更多配色方案](https://iterm2colorschemes.com/)

