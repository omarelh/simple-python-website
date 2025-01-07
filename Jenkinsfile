pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'apt install -y python3-venv'
                sh 'python3 -m venv myenv'
                sh  'source myenv/bin/activate'
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

