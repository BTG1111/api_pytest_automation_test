# Pytest + Allure Automated Testing Project

This project is designed to run API tests and automatically generate Allure test reports.  
It uses Docker / Docker Compose to easily create a consistent testing environment, ensuring smooth CI/CD workflows.

---

## 📦 Project Structure

```bash
.
├── api_requests
│   └── list_users.py
│   └── single_user.py
├── log/
│   └── api_test.log
├── tests/
│   └── test_list_users.py
│   └── test_single_user.py
├── .gitignore
├── base_api.py
├── config
├── docker-compose.yml
├── Dockerfile
├── README.md
├── requirements.txt
└── allure-report/  (auto-generated, not version controlled)
```

## 🛠 Installation and Usage

1. Install Docker & Docker Compose

Please install:
1. [Docker Desktop](https://www.docker.com/) 
2. Docker Compose (built-in with recent Docker Desktop versions)

---

2. Method 1: Using standalone Docker commands

Build Docker Image
```bash
docker build -t pytest-allure .
```

Run the Container and View the Report
```bash
docker run --rm -p 8000:8000 -v ${PWD}:/app pytest-allure
```
- -v ${PWD}:/app: Mount the current directory into the container
- -p 8000:8000: Expose port 8000 to access the report

After running, open your browser and navigate to:
```bash
http://localhost:8000
```

You will see the Allure report generated from the test results.

--- 

3. Method 2: Using docker-compose

To simplify container management, you can use docker-compose.

Build & Run:
```bash
docker-compose up --build
```
This will:
- Automatically build the Docker image
- Start the container
- Run pytest tests
- Generate the Allure report
- Serve the report on port 8000

Then open:
```bash
http://localhost:8000
```
to view the test report.

To stop the container, press Ctrl+C, then clean up:
```bash
docker-compose down
```
---
# 🐳 Dockerfile Overview
- Based on python:3.12-bullseye official image
- Installs Python dependencies
- Installs Allure CLI (for report generation)
-Default container behavior:
  1.	Run pytest tests and save raw results
  2.	Generate Allure HTML reports
  3.	Start a simple Python HTTP server to serve the report

📄 docker-compose.yml Overview

Simplifies container build and run operations. Example content:
```yaml
version: '3'
services:
  pytest-allure:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
 ```