# 公务员考试岗位个性化推荐系统

基于 Streamlit 开发的公务员考试岗位智能推荐系统，使用 2018-2026 年真实岗位数据和进面分数线数据，通过智能匹配、多维度筛选和混合权重推荐算法，帮助考生快速找到合适的岗位。

## ✨ 功能特点

- 📊 **多年份数据** - 支持 2018-2026 年岗位数据查询
- 🎯 **智能匹配** - 根据学历、政治面貌自动筛选可报考岗位
- 🔍 **多维度筛选** - 专业、基层工作经历、工作地点（省市区县三级）
- 🤖 **个性化推荐** - 基于 CRITIC 客观权重 + 业务权重的混合推荐算法
- 📈 **排名与评分** - TOPSIS 综合排序，详细评分明细
- 💾 **数据导出** - 支持将筛选结果导出为 CSV

## 🚀 快速开始

### 在线访问（推荐）

访问部署在 Streamlit Cloud 上的应用：

👉 **[应用地址]**

### 本地运行

```bash
# 1. 克隆项目
git clone [your-repo-url]
cd gwy-recommendation-system

# 2. 安装依赖
pip install -r requirements.txt

# 3. 运行应用
streamlit run src/app.py
```

### Docker 部署

```bash
# Windows
start_docker.bat

# Linux/Mac
chmod +x start_docker.sh
./start_docker.sh
```

## 📁 项目结构

```
gwy-recommendation-system/
├── src/
│   ├── app.py                 # 主应用程序
│   └── preprocess_data.py     # 数据预处理脚本
├── data/
│   ├── cache/                 # Parquet 缓存数据（已提交）
│   │   ├── positions_*.parquet
│   │   └── scores.parquet
│   └── raw/                   # 原始 Excel 数据（未提交）
├── .streamlit/
│   └── config.toml           # Streamlit 配置
├── requirements.txt           # Python 依赖
├── Dockerfile                # Docker 配置
├── docker-compose.yml        # Docker Compose 配置
└── README.md                 # 本文件
```

## 🛠️ 技术栈

- **前端框架**: Streamlit
- **数据处理**: Pandas, NumPy
- **数据格式**: Parquet, Excel
- **推荐算法**: CRITIC 权重法 + TOPSIS 排序法
- **部署平台**: Streamlit Cloud

## 📈 推荐算法说明

系统采用混合权重策略：

1. **CRITIC 客观权重** - 基于数据离散度和相关性自动计算
2. **业务权重** - 基于公务员报考常识的人工设定
3. **混合权重** - 60% CRITIC + 40% 业务权重融合
4. **TOPSIS 排序** - 计算与正负理想解距离，得出相对贴近度

评价指标包括：
- 进面分数（成本型）
- 招考人数（效益型）
- 专业要求数（成本型）
- 机构层级（效益型）
- 学历匹配度（适度型）
- 备注限制数（成本型）

## ☁️ Streamlit Cloud 部署

### 部署步骤

1. **准备 GitHub 仓库**
   ```bash
   # 初始化 Git
   git init
   
   # 添加文件
   git add .
   
   # 提交
   git commit -m "Initial commit: 公务员考试岗位推荐系统"
   
   # 创建 GitHub 仓库并推送
   git remote add origin [your-github-repo-url]
   git branch -M main
   git push -u origin main
   ```

2. **访问 Streamlit Cloud**
   - 打开：https://share.streamlit.io/
   - 使用 GitHub 账号登录

3. **创建新应用**
   - 点击 "New app"
   - 填写以下信息：
     - **Repository**: 选择您的 GitHub 仓库
     - **Branch**: 选择 `main` 分支
     - **Main file path**: 填写 `src/app.py`

4. **部署配置**
   - （可选）点击 "Advanced settings"
   - 可以自定义应用名称和子域名
   - 确保 Python 版本选择 3.9 或更高

5. **开始部署**
   - 点击 "Deploy!" 按钮
   - 等待 2-5 分钟，应用将自动部署完成

6. **完成！**
   - 部署成功后会获得一个可分享的链接
   - 应用地址类似：https://[app-name].streamlit.app

### 数据说明

由于 `data/raw/` 目录下的 Excel 文件较大，`.gitignore` 已将其排除。

✅ **已包含在仓库**：`data/cache/` 目录下的 Parquet 文件，这些是预处理后的高效数据格式，应用可以直接使用。

### 更新部署

当您推送新代码到 GitHub 仓库时，Streamlit Cloud 会自动检测并重新部署应用！

## 📋 使用说明

1. **选择年份和工作表** - 在左侧边栏选择要查询的年份
2. **填写个人信息** - 选择您的学历和政治面貌，系统自动匹配可报考岗位
3. **设置筛选条件** - 输入专业关键词、选择基层工作经历、工作地点
4. **查看筛选结果** - 在主界面查看符合条件的岗位列表
5. **手动删除（可选）** - 勾选并删除您不感兴趣的岗位
6. **查看推荐结果** - 系统自动计算推荐分数并排序
7. **查看评分详情** - 点击选项卡查看权重信息和各岗位评分明细
8. **下载结果** - 点击下载按钮将结果导出为 CSV

## 🔧 配置调整

### 修改业务权重

编辑 `src/app.py` 中的 `business_weights` 字典：

```python
business_weights = {
    '进面分数': 0.35,      # 调整各指标权重
    '招考人数': 0.25,
    '专业要求数': 0.15,
    '机构层级': 0.10,
    '学历匹配': 0.08,
    '备注限制数': 0.07
}
```

### 修改混合权重比例

调整 `alpha` 和 `beta` 参数：

```python
alpha = 0.6  # CRITIC 权重比例
beta = 0.4   # 业务权重比例
```

## 📞 常见问题

**Q: 数据更新了怎么办？**
A: 更新 `data/raw/` 下的 Excel 文件，运行 `src/preprocess_data.py` 重新生成 Parquet 缓存，然后提交到 GitHub。

**Q: 部署失败了怎么办？**
A: 查看 Streamlit Cloud 的日志，检查 `requirements.txt` 依赖是否正确。

**Q: 可以自定义推荐算法吗？**
A: 可以！修改 `src/app.py` 中的 `calculate_recommendation_scores` 函数。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

本项目仅供学习和研究使用。

---

🎉 **祝您找到心仪的岗位！**