pipeline {
    agent any

    stages {
        stage('Build') {
            agent {
                docker {
                    image 'docker:dind'
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