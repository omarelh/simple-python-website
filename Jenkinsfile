pipeline {
    agent any
    stages {
        stage('Run Tests') {
            steps {
                sh 'pytest test/'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t python-app .'
            }
        }
    }
}
