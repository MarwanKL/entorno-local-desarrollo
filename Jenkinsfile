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
                bat 'C:\\Users\\marwa\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\pip.exe install -r requirements.txt'
                bat 'C:\\Users\\marwa\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\pytest.exe --cov=tests/'
            }
        }
        stage('Proceso de lintado') {
            steps {
                bat 'C:\\Users\\marwa\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\flake8.exe'
            }
        }
        stage('Creación de imagen Docker') {
            steps {
                bat 'docker build -t marwaann/repo .'
            }
        }
        stage('Subida del resultado a Docker Hub') {
            when {
                expression { env.BRANCH_NAME == 'develop' || env.BRANCH_NAME == 'master' || env.BRANCH_NAME == 'main' }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', passwordVariable: 'dckr_pat_QjdtktcnEg0K2DbS190ceN6Xj9Q', usernameVariable: 'marwaann')]) {
                    bat 'docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD'
                    bat 'docker push marwaann/repo'
                }
            }
        }
    }
}