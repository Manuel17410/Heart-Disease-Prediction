pipeline{
    agent any

        environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = "savvy-temple-463113-v5"
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

        stage('building and pushing docker image to gcr'){
            steps{
                withCredentials([file(credentialsId: 'gcp-key2' , variable : 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'Building and Pushing Docker Image to GCR.............'
                        sh '''
                        export PATH=$PATH:${GCLOUD_PATH}


                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

                        gcloud config set project ${GCP_PROJECT}

                        gcloud auth configure-docker --quiet

                        docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .

                        docker push gcr.io/${GCP_PROJECT}/ml-project:latest 

                       '''

                    }
                }
            }   
        }
    }
}




// pay attention to name of virtual enviroment and whether this code is for Linux or Windows

