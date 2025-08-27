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
                // Run pytest inside the built image (tests are copied into the image)
                sh 'docker run --rm -w /app jenkins-demo-app:latest ls -la /app'
                sh 'docker run --rm -w /app jenkins-demo-app:latest pytest -q'
            }
        }
        stage('Run Container') {
            steps {
                sh 'docker run -d -p 8081:8081 --name demo-app jenkins-demo-app:latest'
            }
        }
    }
}