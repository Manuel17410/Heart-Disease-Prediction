pipeline {
    agent {
        docker {
            image 'jenkins-agent-python:latest'
            label ''                   // optional
            args '-u root:root'        // run as root
            reuseNode true             // <-- important so Jenkins doesn't override the container
        }
    }

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Debug: Confirm Python Works') {
            steps {
                sh '''
                echo "✅ Python location & version:"
                which python3
                python3 --version
                '''
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                echo "🐍 Setting up virtual environment..."
                python3 -m venv $VENV_DIR
                . $VENV_DIR/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        // Add more stages here if needed
    }
}






