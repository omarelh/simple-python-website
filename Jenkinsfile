pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }
    }
}
