# Streamlit Cloud 部署指南

## 🚀 快速开始（必读！

### 第一步：准备 GitHub 仓库

#### 1. 检查项目文件

确保项目已为您准备好了所有需要的文件：

✅ `README.md` - 项目说明
✅ `requirements.txt` - 依赖列表
✅ `src/app.py` - 主应用
✅ `data/cache/` - 预处理后的数据（约7MB
✅ `.streamlit/config.toml` - 配置文件
✅ `.gitignore` - Git 忽略配置

#### 2. 初始化 Git 仓库

打开命令行（CMD、PowerShell 或 Git Bash，进入项目目录：

```bash
cd "c:\Users\xzy\Desktop\2\项目代码"
```

初始化 Git（如果还没有初始化）：

```bash
git init
```

#### 3. 配置 Git 用户信息（首次使用）：

```bash
git config user.name "您的名字"
git config user.email "您的邮箱@example.com"
```

#### 4. 添加文件到暂存区：

```bash
git add .
```

#### 5. 提交更改：

```bash
git commit -m "Initial commit: 公务员考试岗位推荐系统"
```

### 第二步：创建 GitHub 仓库

#### 方式一：使用 GitHub 网站

1. 访问 https://github.com/ 并登录
2. 点击右上角的 "+" 号 → "New repository"
3. 填写信息：
   - Repository name: `gwy-recommendation-system（或您喜欢的名字）
   - Description: "公务员考试岗位个性化推荐系统
   - Public/Private: 选择 Public（免费）
   - **不要**勾选 "Add a README file"
   - **不要**勾选 "Add .gitignore"
   - **不要**勾选 "Choose a license"
4. 点击 "Create repository"

#### 方式二：使用 GitHub Desktop（更简单！

1. 下载安装 GitHub Desktop：https://desktop.github.com/
2. 打开 GitHub Desktop，登录 GitHub 账号
3. 点击 File → Add Local Repository
4. 选择项目目录：`c:\Users\xzy\Desktop\2\项目代码`
5. 点击 Publish repository
6. 填写仓库名称，选择 Public，点击 Publish Repository

#### 推送到 GitHub（命令行方式）：

创建仓库后，按 GitHub 会显示推送命令，类似：

```bash
git remote add origin https://github.com/您的用户名/gwy-recommendation-system.git
git branch -M main
git push -u origin main
```

### 第三步：部署到 Streamlit Cloud！

1. **访问 Streamlit Cloud**
   - 打开：https://share.streamlit.io/
   - 使用您的 GitHub 登录（如果没有账号，先注册）

2. **授权访问**
   - 点击 "New app" 或 "Create app"
   - 可能需要授权访问您的仓库权限

3. **填写部署设置：
   
   | 设置项 | 值 |
   |---------|-----|
   | **Repository** | 选择刚才创建的仓库（如：您的用户名/gwy-recommendation-system） |
   | **Branch** | 选择 `main` |
   | **Main file path** | 填写 `src/app.py` ⚠️ 重要！一定要填这个！ |

4. **（可选）自定义应用名称**
   - 点击 "Advanced settings"（可选）
   - App URL 中可以自定义子域名
   - Python version：选 3.9 或 3.11

5. **点击 "Deploy!" 按钮！✨

6. **等待部署完成（2-5分钟）

   您会看到进度条，显示正在安装依赖、启动应用

7. **🎉 完成！

   部署成功后，您会获得一个链接，类似：
   `https://gwy-recommendation-system.streamlit.app/`

### 第四步：分享您的应用！

- 复制链接，分享给朋友、同学或老师！

---

## 📝 详细步骤图解

### 1. GitHub 仓库创建详细步骤

1. 访问 https://github.com/new

2. 填写仓库信息：
   ```
   Repository name: gwy-recommendation-system
   Description: 公务员考试岗位个性化推荐系统
   Public/Private: Public
   ```

3. 点击 "Create repository"

4. 复制仓库页面会显示推送命令，按照执行即可

### 2. 命令行完整操作流程

打开 PowerShell 或 CMD：

```powershell
# 1. 进入项目目录
cd "c:\Users\xzy\Desktop\2\项目代码"

# 2. 初始化 Git（如果还没初始化）
git init

# 3. 检查当前状态（应该看到很多文件）
git status

# 4. 添加所有文件
git add .

# 5. 提交
git commit -m "Initial commit: 公务员考试岗位推荐系统"

# 6. 关联远程仓库（替换为您的实际仓库地址）
git remote add origin https://github.com/您的用户名/gwy-recommendation-system.git

# 7. 重命名分支（确保是 main）
git branch -M main

# 8. 推送到 GitHub
git push -u origin main
```

### 3. Streamlit Cloud 部署界面

登录后：

```
┌─────────────────────────────────────────────────────────┐
│ Deploy a new app                                         │
├─────────────────────────────────────────────────────────┤
│ Repository: [您的用户名/gwy-recommendation-system   ▼ │
│ Branch:     [main ▼                                      │
│ Main file:  src/app.py                           │
│                                                         │
│ [ Advanced settings...  自定义域名、Python版本            │
│                                                         │
│ [Deploy!]                                              │
└─────────────────────────────────────────────────────────┘
```

### 4. 查看部署日志

部署中会看到：
- ✅ Cloning repository
- ✅ Installing dependencies
- ✅ Starting app
- ✅ Deployed! 🎉

---

## ⚠️ 常见问题

### Q1: Main file path 填什么？

**一定要填：`src/app.py`

**注意！不能填：** `app.py` 或其他值！

### Q2: 数据文件会上传吗？

✅ 会！`data/cache/` 目录下的所有文件已配置为上传，这些是处理后的高效数据格式，约7MB，完全没问题。

`data/raw/` 原始Excel大文件被 `.gitignore` 排除了，不会上传。

### Q3: 部署失败怎么办？

1. **查看日志** - Streamlit Cloud 界面显示的"View logs"
2. **检查依赖** - 确认 `requirements.txt` 中的包正确
3. **检查文件路径** - 确认 `src/app.py` 路径正确
4. **重试部署** - 点击菜单 → Redeploy

### Q4: 如何更新应用？

**非常简单！只要您只需要：

```bash
# 修改代码后
git add .
git commit -m "更新描述"
git push
```

Streamlit Cloud 会自动检测 GitHub 的推送并重新部署！

### Q5: 想换个更好记的域名？

1. 登录 Streamlit Cloud，点击设置 → 点击"Change subdomain，自定义子域名

### Q6: 数据更新？

有新数据时：

1. 更新 `data/raw/` 下的 Excel
2. 运行 `python src/preprocess_data.py 重新生成 cache 后数据
3. Git 并推送

---

## ✅ 检查清单

部署前请确认：

- [ ] README.md 存在
- [ ] requirements.txt 存在
- [ ] src/app.py 存在
- [ ] data/cache/ 目录有 parquet 文件
- [ ] .gitignore 配置正确（没有排除了 data/raw/）
- [ ] GitHub 仓库已创建并推送
- [ ] Streamlit Cloud 已连接 GitHub 账号
- [ ] Streamlit Cloud 部署时 Repository 选对了仓库
- [ ] Streamlit Cloud 部署时 Branch 选 main
- [ ] Streamlit Cloud 部署时 Main file path 填 src/app.py

---

## 📌 快速命令速查表

| 操作 | 命令 |
|-----|------|
| 查看状态 | git status |
| 添加所有文件 | git add . |
| 提交 | git commit -m "信息" |
| 推送到 GitHub | git push |
| 拉取更新 | git pull |
| 查看远程仓库 | git remote -v |

---

## 🎯 快速开始（最简版）

### 五分钟内完成部署！

1. **打开 PowerShell**
```powershell
cd "c:\Users\xzy\Desktop\2\项目代码"
git init
git add .
git commit -m "Initial commit"
```

2. **GitHub 建新仓库**
```bash
git remote add origin https://github.com/您的用户名/gwy-recommendation-system.git
git branch -M main
git push -u origin main
```

3. **访问 share.streamlit.io → New app → 选填 → Deploy!

---

## 💡 提示

- Streamlit 免费额度非常充足！免费额度：
- 每月 100GB 带宽
- 足够个人应用 24 小时运行
- 完全免费！

---

## 🎉 部署成功！

恭喜您就可以复制链接，开始使用吧！

---

## 📞 需要帮助？

查看 README.md 或者 Streamlit 官方文档：https://docs.streamlit.io/streamlit-cloud