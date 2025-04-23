pipeline {
    agent any

    environment {
    DOCKER_COMPOSE_CMD = "docker compose"
    WORKSPACE_DIR = "${env.WORKSPACE}"
}

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning the repository'
                checkout scm
            }
        }

        stage('Setup docker-compose') {
            steps {
                sh '''
                    mkdir -p ~/.docker/cli-plugins/
                    curl -SL https://github.com/docker/compose/releases/download/v2.27.0/docker-compose-linux-x86_64 -o ~/.docker/cli-plugins/docker-compose
                    chmod +x ~/.docker/cli-plugins/docker-compose
                    docker compose version
                '''
            }
        }

        stage('Run Docker Compose') {
            steps {
                script {
                    echo 'Starting docker compose with correct WORKSPACE volume...'
                    sh """
                        export WORKSPACE=${WORKSPACE_DIR}
                        docker compose down || true
                        docker compose up -d --build
                    """
                    echo 'echo "Workspace content after docker-compose up:"'
                    sh 'ls -alh /var/jenkins_home/workspace/Pytest-Allure'
                    sh "${DOCKER_COMPOSE_CMD} exec pytest-allure ls -alh /app"

                }
            }
        }

        stage('Copy Workspace to Container') {
            steps {
                script {
                    echo 'Copying workspace content to the container...'
                    sh "docker cp ${WORKSPACE_DIR}/. pytest-allure:/app"
                }
            }
        }

        stage('Archive Allure Results in Container') {
            steps {
                script {
                    echo 'Archiving Allure results in the container...'
                    sh "${DOCKER_COMPOSE_CMD} exec pytest-allure tar -czf /tmp/allure-results.tar.gz -C /app allure-results"
                }
            }
        }

        stage('Copy Allure Archive') {
            steps {
                script {
                    echo 'Copying Allure results archive to Jenkins workspace...'
                    sh "${DOCKER_COMPOSE_CMD} cp pytest-allure:/tmp/allure-results.tar.gz ."
                }
            }
        }

        stage('Extract Allure Archive') {
            steps {
                script {
                    echo 'Extracting Allure results archive in Jenkins workspace...'
                    sh 'tar -xzf allure-results.tar.gz'
                }
            }
        }

        stage('Run Pytest and Generate Allure Report') {
            steps {
                script {
                    echo 'Running pytest inside container...'
                    sh "${DOCKER_COMPOSE_CMD} exec pytest-allure pytest tests/ --alluredir=./allure-results"
                    }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up containers'
            sh "${DOCKER_COMPOSE_CMD} down"

            echo 'Publishing Allure report...'
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]

        }
        success {
            echo 'Build and tests completed successfully!'
        }
        failure {
            echo 'Build or tests failed!'
        }
    }
}
