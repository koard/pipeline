pipeline {
  agent any
  parameters {
    booleanParam(name: 'RUN_DEPLOY', defaultValue: true, description: 'Should we deploy?')
    choice(name: 'ENV', choices: ['dev', 'staging', 'prod'], description: 'Select environment')
  }
  stages {
    stage('Build') {
      steps {
        echo 'Building application...'
        // simulate build
        sh 'echo Build done'
      }
    }
    stage('Test in Parallel') {
      parallel {
        stage('Unit Tests') {
          steps {
            echo 'Running unit tests...'
            sh 'python3 -m unittest test_hello.py'
            sh 'echo "All tests passed!" > results.txt'
            archiveArtifacts artifacts: 'results.txt', fingerprint: true
          }
        }
        stage('Integration Tests') {
          steps {
            echo 'Running integration tests...'
            sh 'sleep 5'
          }
        }
      }
    }
    stage('Simulate OS Testing') {
      parallel {
        stage('Linux Test') {
          steps {
            echo 'Simulating test on Linux...'
            sh 'echo "This is Linux test simulation."'
          }
        }
        stage('Windows Test') {
          steps {
            echo 'Simulating test on Windows...'
            sh 'echo "This is Windows test simulation."'
          }
        }
      }
    }
    stage('Approval') {
      when {
        expression { return params.RUN_DEPLOY }
      }
      steps {
        timeout(time: 2, unit: 'MINUTES') {
          input message: "Do you want to proceed with deployment?"
        }
      }
    }
    stage('Deploy') {
      when {
        expression { return params.RUN_DEPLOY }
      }
      steps {
        echo "Deploying application to ${params.ENV} environment..."
        // simulate deploy
        sh 'echo Deploy done'
      }
    }
  }
  post {
    success {
      echo '✅ Pipeline finished successfully!'
    }
    failure {
      echo '❌ Pipeline failed. Check logs!'
    }
    always {
      echo 'Pipeline completed (success or failure).'
    }
  }
}
