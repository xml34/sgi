pipeline {
    agent {
        docker {
            image 'docker:latest'
            args '-v /var/run/docker.sock:/var/run/docker.sock -u root'
        }
    }

    environment {
        SECRETS_DIR = "${WORKSPACE}/secrets"
    }

    stages {
        stage('Prepare Secrets') {
            steps {
                script {
                    // Ensure the secrets directory exists
                    sh 'rm -f $SECRETS_DIR/pg.ini'
                    sh 'rm -f $SECRETS_DIR/alembic.ini'
                    //sh 'mkdir -p $SECRETS_DIR'
                    sh 'apk update && apk add make'
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
            /*agent {
                docker {
                    image 'docker:dind'
                    reuseNode true
                }
            }*/
            steps {
                echo 'Building...     -   -   -   -   -   -   -   -   -   -   - '
                sh 'docker --version'
                // sh 'make build'
                sh 'docker-compose build'
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
    post {
        always {
            junit 'tests/integration/reports/report.xml'
            publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, icon: '', keepAll: false, reportDir: 'tests/integration/reports', reportFiles: 'report.html', reportName: 'SGI HTML Report', reportTitles: '', useWrapperFileDirectly: true])
        }
    }
}