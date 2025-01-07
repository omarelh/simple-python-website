pipeline {
    agent {
        docker { image 'python:3.10' }
    }
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t python-app .'
            }
        }
    }
}
