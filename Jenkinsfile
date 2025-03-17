pipeline {
    agent any

    stages {
        stage('Build') {
            agent {
                docker {
                    image 'docker:latest-alpine'
                    reuseNode true
                }
            }
            steps {
                echo 'Building..'
                sh 'docker --version'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}