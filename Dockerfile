# 使用官方的 Python 映像
FROM python:3.10

# 設置工作目錄
WORKDIR /app

# 複製所有文件到工作目錄
COPY . /app

# 安裝必要的包
RUN pip install --no-cache-dir -r requirements.txt

# 暴露 Streamlit 默認端口
EXPOSE 8501

# 運行 Streamlit 應用
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
