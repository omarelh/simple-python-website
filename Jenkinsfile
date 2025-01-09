pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pipx install requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }
    }
}

