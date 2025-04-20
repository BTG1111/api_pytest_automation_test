# 用官方 Python  版
FROM python:3.12-bullseye

# 安裝必要工具
RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-11-jdk wget unzip curl \
    && rm -rf /var/lib/apt/lists/*

# 安裝 Allure CLI
RUN wget https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.tgz \
    && tar -zxvf allure-2.27.0.tgz -C /opt/ \
    && ln -s /opt/allure-2.27.0/bin/allure /usr/bin/allure \
    && rm allure-2.27.0.tgz

# 安裝Python套件
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 設定工作目錄
WORKDIR /app

# 複製專案進來
COPY . .

# 預設執行
CMD pytest tests/ --alluredir=./report && \
    allure generate ./report -o ./allure-report --clean && \
    cd allure-report && python3 -m http.server 8000