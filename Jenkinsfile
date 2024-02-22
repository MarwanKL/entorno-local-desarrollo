pipeline {
    agent any
    stages {
        stage('Clonado de código fuente') {
            steps {
                checkout scm
            }
        }
        stage('Ejecución de tests') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest'
            }
        }
        stage('Proceso de lintado') {
            steps {
                sh 'flake8'
            }
        }
        stage('Creación de imagen Docker') {
            steps {
                sh 'docker build -t marwaann/repo .'
            }
        }
        stage('Subida del resultado a Docker Hub') {
            when {
                expression { env.BRANCH_NAME == 'develop' || env.BRANCH_NAME == 'master' || env.BRANCH_NAME == 'main' }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', passwordVariable: 'dckr_pat_QjdtktcnEg0K2DbS190ceN6Xj9Q', usernameVariable: 'marwaann')]) {
                    sh 'docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD'
                    sh 'docker push marwaann/repo'
                }
            }
        }
    }
}