pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }
    }
}

