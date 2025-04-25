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
├── configuration
│   └── Dockerfile
├── log/
│   └── api_test.log (auto-generated)
├── tests/
│   └── test_list_users.py
│   └── test_single_user.py
├── .gitignore
├── base_api.py
├── config
├── conftest
├── docker-compose.yml
├── Dockerfile
├── README.md
├── requirements.txt
└── allure-report/  (auto-generated, not version controlled)
```

## 🛠 Installation and Usage

### Install Docker & Docker Compose

Please install:
1. [Docker Desktop](https://www.docker.com/) 
2. Docker Compose (built-in with recent Docker Desktop versions)

---

## Method 1: Using standalone Docker commands

Build Docker Image
```bash
docker build -t pytest-allure -f configuration/Dockerfile .
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

## Method 2: Pytest + Allure Report CI/CD with Jenkins (Docker)

Below steps demonstrate how to use Jenkins (Dockerized) to run Pytest tests and generate an Allure Report.


### Workflow Overview:
1. Set up a Jenkins Docker container
2. Install required plugins (Pipeline, Allure, etc.)
3. Create a Jenkins pipeline job (with SCM integration)
4. Jenkins checks out the project code
5. Start the test environment using docker-compose
6. Run pytest inside the container
7. Generate Allure test results
8. View the Allure Report from Jenkins

### Step-by-Step Instructions

#### 1. Set Up Jenkins in Docker
```bash
docker pull jenkins/jenkins:lts

docker run -d --name jenkins \
  -u root \
  -p 8080:8080 \
  -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkins/jenkins:lts
```
🚀 Notes
- -v /var/run/docker.sock allows Jenkins container to control the Docker daemon.
- Access Jenkins UI at http://localhost:8080
- Jenkins data persists under jenkins_home.

#### 2. Install Required Jenkins Plugins

Inside Jenkins UI → Manage Jenkins → Manage Plugins → Install:
- Pipeline
- Docker Pipeline
- Allure Report Plugin
- Git Plugin

#### 3. Create a Jenkins Job

1. Create a new Pipeline job. 
   - Name: `pytest-allure`  # you can enter any name you prefer
   - Type: Pipeline
2. Configure:
   - Pipeline script from SCM
   - Choose Git and enter your repository URL
   - Branch Specifier: */main (or your branch)
   - Script Path: Jenkinsfile

#### 4. Configure Allure Commandline Tool in Jenkins
After installing the Allure Report Plugin, you also need to configure the Allure Commandline tool:
1. In Jenkins UI → Manage Jenkins → Global Tool Configuration 
2. Find the section Allure Commandline 
3. Click Add Allure Commandline 
4. Set a name, for example: Allure

#### 5. Start the Test Execution

In Jenkins, simply click Build Now.
Wait for the pipeline to complete.

#### 6. View the Allure Report
- Go to your Jenkins job.
- Click on the Allure Report link on the left sidebar.
- View your test results beautifully presented!
