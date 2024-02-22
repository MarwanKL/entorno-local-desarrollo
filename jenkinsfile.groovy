pipeline {
    agent any

    stages {
        stage('Clonado de código fuente') {
            steps {
                git 'https://tu-usuario@tu-repo.git'
            }
        }

        stage('Ejecución de tests') {
            steps {
                sh 'python -m pytest'
            }
        }

        stage('Proceso de lintado') {
            steps {
                sh 'flake8'
            }
        }

        stage('Creación de imagen Docker') {
            steps {
                script {
                    // Lógica para construir la imagen Docker
                }
            }
        }

        stage('Subida a Registry') {
            when {
                expression { currentBuild.resultIsBetterOrEqualTo('SUCCESS') }
            }
            steps {
                script {
                    // Lógica para subir la imagen Docker al Registry
                }
            }
        }
    }
}
