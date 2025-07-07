pipeline{
    agent any

        environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = "mlops-new-447207"
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
    }

    stages{
        stage('Cloning Github repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github repo to Jenkins............'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token2', url: 'https://github.com/Manuel17410/Heart-Disease-Prediction.git']])
                }
            }   
        }

        stage('Setting up our virtual enviroment and isntalling dependencies'){
            steps{
                script{
                    echo 'Setting up our virtual enviroment and isntalling dependencies............'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }   
        }
    }
}




// pay attention to name of virtual enviroment and whether this code is for Linux or Windows

