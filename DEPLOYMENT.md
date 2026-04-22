# 公务员考试岗位个性化推荐系统 - 部署指南

## 项目简介

这是一个基于Streamlit开发的公务员考试岗位个性化推荐系统，使用2018-2026年真实岗位数据和进面分数线数据，通过智能匹配、筛选和个性化推荐算法，帮助考生找到合适的岗位。

## 快速开始

### 方式一：Docker部署（推荐）

#### Windows系统

```bash
# 双击运行或命令行执行
start_docker.bat
```

#### Linux/Mac系统

```bash
chmod +x start_docker.sh
./start_docker.sh
```

#### 手动Docker部署

```bash
# 1. 构建镜像
docker-compose build

# 2. 启动服务
docker-compose up -d

# 3. 查看日志
docker-compose logs -f
```

### 方式二：本地直接运行

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 运行应用
streamlit run src/app.py
```

## 访问地址

部署成功后，通过以下地址访问：

- 本地访问：http://localhost:8501
- 局域网访问：http://[服务器IP]:8501

## 常用命令

### Docker命令

```bash
# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down

# 重启服务
docker-compose restart

# 更新并重新部署
docker-compose down
docker-compose build
docker-compose up -d
```

### 本地开发命令

```bash
# 运行应用
streamlit run src/app.py

# 指定端口运行
streamlit run src/app.py --server.port=8501
```

## 云平台部署

### 1. 阿里云/腾讯云部署

#### 步骤1：购买云服务器

选择配置：
- 操作系统：Ubuntu 20.04/22.04 或 CentOS 7+
- CPU：2核及以上
- 内存：4GB及以上
- 硬盘：40GB及以上

#### 步骤2：安装Docker

```bash
# Ubuntu/Debian
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# 启动Docker
sudo systemctl start docker
sudo systemctl enable docker

# 安装Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

#### 步骤3：上传项目代码

```bash
# 使用SCP或FTP工具上传项目到服务器
# 或使用Git克隆

# 进入项目目录
cd /path/to/project
```

#### 步骤4：启动服务

```bash
# 给脚本添加执行权限
chmod +x start_docker.sh

# 运行部署脚本
./start_docker.sh
```

#### 步骤5：配置防火墙

```bash
# Ubuntu UFW
sudo ufw allow 8501

# CentOS firewalld
sudo firewall-cmd --permanent --add-port=8501/tcp
sudo firewall-cmd --reload
```

### 2. Streamlit Cloud部署

1. 将代码推送到GitHub仓库
2. 访问 https://share.streamlit.io/
3. 使用GitHub账号登录
4. 点击 "New app"
5. 填写仓库信息：
   - Repository: 您的GitHub仓库
   - Branch: main
   - Main file path: src/app.py
6. 点击 "Deploy" 完成部署

### 3. Render部署

1. 访问 https://render.com/
2. 注册并登录
3. 点击 "New" -> "Web Service"
4. 连接GitHub仓库
5. 配置：
   - Runtime: Docker
   - Region: 选择就近区域
   - Instance Type: Starter或更高
6. 点击 "Create Web Service" 完成部署

### 4. Railway部署

1. 访问 https://railway.app/
2. 注册并登录
3. 点击 "New Project"
4. 选择 "Deploy from repo"
5. 选择您的GitHub仓库
6. 配置变量（如需要）
7. 点击 "Deploy" 完成部署

## 域名绑定

### 使用Nginx反向代理

创建 `/etc/nginx/sites-available/gwy-app` 文件：

```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    location / {
        proxy_pass http://127.0.0.1:8501;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # WebSocket支持
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

启用配置：

```bash
sudo ln -s /etc/nginx/sites-available/gwy-app /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

### SSL证书配置（HTTPS）

使用Let's Encrypt免费证书：

```bash
# 安装Certbot
sudo apt update
sudo apt install certbot python3-certbot-nginx

# 获取并安装证书
sudo certbot --nginx -d your-domain.com

# 自动续期
sudo certbot renew --dry-run
```

## 性能优化

### 1. Streamlit配置

编辑 `.streamlit/config.toml` 优化性能。

### 2. 数据缓存

项目已使用Parquet格式缓存数据，大幅提升加载速度。

### 3. 服务器资源

根据访问量调整服务器配置，建议：
- 低访问量：2核4GB
- 中等访问量：4核8GB
- 高访问量：8核16GB+

## 安全建议

1. 定期更新系统和软件包
2. 配置防火墙限制访问
3. 使用HTTPS加密传输
4. 定期备份数据
5. 不要在生产环境中暴露敏感信息

## 故障排查

### 查看日志

```bash
# Docker日志
docker-compose logs -f

# 本地日志
# 运行时直接在终端查看
```

### 常见问题

**问题：服务无法启动**
- 检查端口8501是否被占用
- 检查Docker是否正常运行
- 查看日志排查错误

**问题：数据加载失败**
- 检查data目录是否存在
- 检查文件权限
- 确认数据文件完整性

**问题：访问速度慢**
- 检查服务器资源使用
- 优化Streamlit配置
- 考虑使用CDN加速

## 备份与恢复

### 数据备份

```bash
# 备份data目录
tar -czf gwy-data-backup-$(date +%Y%m%d).tar.gz data/
```

### Docker备份

```bash
# 备份镜像
docker save -o gwy-app-image.tar gwy-app:latest

# 备份容器
docker export gwy-app-container > gwy-app-container.tar
```

## 联系方式

如有问题，请查看项目文档或联系维护人员。

---

**祝您部署顺利！🎉**