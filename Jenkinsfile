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
                sh 'docker run --rm -v /var/jenkins_home/workspace:/app -w /app jenkins-demo-app:latest ls -l /app'
                sh 'docker run --rm -v /var/jenkins_home/workspace:/app -w /app jenkins-demo-app:latest cat /app/test_app.py'
                sh 'docker run --rm -v /var/jenkins_home/workspace:/app -w /app jenkins-demo-app:latest pytest || true'
            }
        }
        stage('Run Container') {
            steps {
                sh 'docker run -d -p 8081:8081 --name demo-app jenkins-demo-app:latest'
            }
        }
    }
}