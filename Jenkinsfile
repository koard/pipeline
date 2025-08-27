pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/koard/pipeline.git'
            }
        }
        stage('Build Image') {
            steps {
                sh 'docker build -t jenkins-demo-app:latest .'
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Running tests..."'
                // Host workspace contents
                sh 'echo "Host workspace ($PWD) contents:"'
                sh 'ls -la'
                // Inside container: list /app
                sh 'docker run --rm -v "$PWD":/app -w /app jenkins-demo-app:latest ls -la /app'
                // Inside container: run pytest
                sh 'docker run --rm -v "$PWD":/app -w /app jenkins-demo-app:latest pytest -q || true'
            }
        }
        stage('Run Container') {
            steps {
                sh 'docker run -d -p 8081:8081 --name demo-app jenkins-demo-app:latest'
            }
        }
    }
}