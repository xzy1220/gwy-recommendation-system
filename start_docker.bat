@echo off
echo ========================================
echo 公务员考试岗位个性化推荐系统 - 部署
echo ========================================
echo.

echo [1/4] 检查Docker...
docker --version
if errorlevel 1 (
    echo 错误: 未找到Docker，请先安装Docker Desktop
    pause
    exit /b 1
)

echo.
echo [2/4] 构建Docker镜像...
docker-compose build

echo.
echo [3/4] 启动服务...
docker-compose up -d

echo.
echo [4/4] 等待服务启动...
timeout /t 10 /nobreak >nul

echo.
echo ========================================
echo 部署完成！
echo ========================================
echo.
echo 访问地址: http://localhost:8501
echo.
echo 查看日志: docker-compose logs -f
echo 停止服务: docker-compose down
echo 重启服务: docker-compose restart
echo.
pause