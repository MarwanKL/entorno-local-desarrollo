pipeline {
    agent any

    stages {
        stage('Clonado de código fuente') {
            steps {
                echo 'Clonando el código fuente...'
                checkout scm
            }
        }

        stage('Ejecución de tests') {
            steps {
                echo 'Ejecutando tests...'
                // Coloca aquí los comandos para ejecutar tus tests
            }
        }

        stage('Proceso de lintado') {
            steps {
                echo 'Realizando lintado...'
                // Coloca aquí los comandos para el lintado con flake8 u otra herramienta
            }
        }

        stage('Creación de imagen Docker') {
            steps {
                echo 'Construyendo la imagen Docker...'
                // Coloca aquí los comandos para construir la imagen Docker
            }
        }

        stage('Subida del resultado') {
            when {
                expression { env.BRANCH_NAME == 'develop' || env.BRANCH_NAME == 'master' || env.BRANCH_NAME == 'main' }
            }
            steps {
                echo 'Subiendo el resultado a algún Registry...'
                // Coloca aquí los comandos para subir el resultado a tu Registry
            }
        }
    }
}
