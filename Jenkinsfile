pipeline {
    agent {
        docker {
            image 'python:3.11.3'
            reuseNode true
        }
    }

    environment {
        SECRETS_DIR = "${WORKSPACE}/secrets"
        INTEGRATION_TEST_REPORTS_DIR="tests/integration/reports"
        UNIT_TEST_REPORTS_DIR="tests/unit/reports"
    }


    stages {
        stage('Build') {
            steps {
                echo 'Building...     -   -   -   -   -   -   -   -   -   -   - '
                sh 'pip install poetry'
                sh 'poetry install'
            }
        }
        stage('Lint Test') {
            steps {
                echo 'Lint Testing..   -   -   -   -   -   -   -   -   -   -   -'
                sh 'poetry run pre-commit run --all-files'
            }
        }
        stage('Unit Test') {
            steps {
                echo 'Unit Testing..   -   -   -   -   -   -   -   -   -   -   -'
                sh 'mkdir -p tests/unit/reports'
                sh 'poetry run pytest tests/unit --junitxml=${UNIT_TEST_REPORTS_DIR}/report.xml --html=${UNIT_TEST_REPORTS_DIR}/report.html'

            }
            post {
                always {
                    junit 'tests/unit/reports/report.xml'
                    publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, icon: '', keepAll: false, reportDir: 'tests/unit/reports', reportFiles: 'report.html', reportName: 'SGI Unit Report', reportTitles: '', useWrapperFileDirectly: true])
                }
            }
        }
        stage('Integration Test') {
            steps {
                echo 'Integration Testing..   -   -   -   -   -   -   -   -   - '
                sh 'mkdir -p tests/integration/reports'
                sh 'poetry run pytest tests/integration --junitxml=${INTEGRATION_TEST_REPORTS_DIR}/report.xml --html=${INTEGRATION_TEST_REPORTS_DIR}/report.html'
            }
            post {
                always {
                    junit 'tests/integration/reports/report.xml'
                    publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, icon: '', keepAll: false, reportDir: 'tests/integration/reports', reportFiles: 'report.html', reportName: 'SGI Inte Report', reportTitles: '', useWrapperFileDirectly: true])
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