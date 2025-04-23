FROM python:3.12-bullseye

# Install Java and other dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-11-jdk wget unzip curl \
    && rm -rf /var/lib/apt/lists/*

# Install Allure CLI
RUN wget https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.tgz \
    && tar -zxvf allure-2.27.0.tgz -C /opt/ \
    && ln -s /opt/allure-2.27.0/bin/allure /usr/bin/allure \
    && rm allure-2.27.0.tgz

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory
WORKDIR /app

# Copy the contents of the current directory to /app in the container
COPY . .

# Expose the port the app runs on
CMD pytest tests/ --alluredir=./report && \
    allure generate ./report -o ./allure-report --clean && \
    cd allure-report && python3 -m http.server 8000