pipeline {
    agent any

    environment {
        SECRETS_DIR = "${WORKSPACE}/secrets"
    }

    stages {
        stage('Prepare Secrets') {
            steps {
                script {
                    // Ensure the secrets directory exists
                    sh 'mkdir -p $SECRETS_DIR'
                }
                // Copy the secret files
                withCredentials([
                    file(credentialsId: 'postgres-ini', variable: 'POSTGRES_INI'),
                    file(credentialsId: 'alembic-ini', variable: 'ALEMBIC_INI')
                ]) {
                    sh 'cp $POSTGRES_INI $SECRETS_DIR/pg.ini'
                    sh 'cp $ALEMBIC_INI $SECRETS_DIR/alembic.ini'
                    sh 'ls secrets'
                }
            }
        }
        stage('Build') {
            agent {
                docker {
                    image 'docker:dind'
                    reuseNode true
                }
            }
            steps {
                echo 'Building...     -   -   -   -   -   -   -   -   -   -   - '
                sh 'make build'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing..        -   -   -   -   -   -   -   -   -   -   -'
                sh '''
                    make test
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..      -   -   -   -   -   -   -   -   -   -   -'
            }
        }
    }
}