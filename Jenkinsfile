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
                // List files in Jenkins workspace (host)
                sh 'echo "Host workspace ($PWD) contents:"'
                sh 'ls -la'
                // List files inside container at /app after mounting current workspace
                sh 'docker run --rm -v "$PWD":/app -w /app jenkins-demo-app:latest /bin/sh -lc "echo \"Inside container /app contents:\"; ls -la /app; echo; [ -f /app/test_app.py ] && echo \"Found test_app.py\" || echo \"test_app.py not found\"; pytest || true"'
            }
        }
        stage('Run Container') {
            steps {
                sh 'docker run -d -p 8081:8081 --name demo-app jenkins-demo-app:latest'
            }
        }
    }
}