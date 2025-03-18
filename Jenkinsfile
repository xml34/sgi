pipeline {
    agent any

    environment {
        SECRETS_DIR = "secrets"
    }

    stages {
        stage('Retrieve Secrets') {
            steps {
                script {
                    def secretsDir = "$env.WORKSPACE/$SECRETS_DIR"
                    // sh "mkdir -p ${secretsDir}"

                    withCredentials([
                        file(credentialsId: 'postgres-ini', variable: 'POSTGRES_INI'),
                        file(credentialsId: 'alembic-ini', variable: 'ALEMBIC_INI')
                    ]) {
                        sh "cp $POSTGRES_INI $secretsDir/alembic.ini"
                        sh "cp $ALEMBIC_INI $secretsDir/pg.ini"
                    }
                }
                sh '''
                    test -f ${SECRETS_DIR}/alembic.ini
                    test -f ${SECRETS_DIR}/pg.ini
                '''
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
                test -
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