# 基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器中
COPY . .

# 使用国内的 PyPI 镜像源并升级 pip
RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple --timeout=120

# 安装项目依赖并使用国内的 PyPI 镜像源
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --timeout=120

# 暴露端口
EXPOSE 8030

# 运行应用程序
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8030"]
