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
                echo 'Secrets...      -   -   -   -   -   -   -   -   -   -   - '
                script {
                    // Ensure the secrets directory exists
                    sh 'rm -f $SECRETS_DIR/pg.ini'
                    sh 'rm -f $SECRETS_DIR/alembic.ini'
                    //sh 'mkdir -p $SECRETS_DIR'
                    sh "sed -i 's/dl-cdn.alpinelinux.org/mirrors.dotsrc.org/' /etc/apk/repositories"
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
            steps {
                echo 'Building...     -   -   -   -   -   -   -   -   -   -   - '
                sh 'docker --version'
                sh 'docker-compose build'
            }
        }


        stage('Lint Test') {
            steps {
                echo 'Lint Testing..   -   -   -   -   -   -   -   -   -   -   -'
                sh 'make linter'
            }
        }
        stage('Unit Test') {
            steps {
                echo 'Unit Testing..   -   -   -   -   -   -   -   -   -   -   -'
                sh 'make unit_test'
            }
            post {
                always {
                    junit 'tests/unit/reports/report.xml'
                    publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, icon: '', keepAll: false, reportDir: 'tests/unit/reports', reportFiles: 'report.html', reportName: 'SGI HTML Report', reportTitles: '', useWrapperFileDirectly: true])
                }
            }
        }
        stage('Integration Test') {
            steps {
                echo 'Integration Testing..   -   -   -   -   -   -   -   -   - '
                sh 'make integration_test'
            }
            post {
                always {
                    junit 'tests/integration/reports/report.xml'
                    publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, icon: '', keepAll: false, reportDir: 'tests/integration/reports', reportFiles: 'report.html', reportName: 'SGI HTML Report', reportTitles: '', useWrapperFileDirectly: true])
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..      -   -   -   -   -   -   -   -   -   -   -'
            }
        }
    }
}