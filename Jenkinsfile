pipeline {
    agent any

    environment {
        JAVA_HOME = tool name: 'JDK', type: 'jdk'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }

        stage('Test') {
            steps {
                sh 'mvn test'
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "Deploying the application"'
                // Add deployment steps here, e.g., deploying to a server or container
            }
        }
    }

    post {
        success {
            emailext subject: 'Build Success: ${currentBuild.fullDisplayName}',
                body: 'The build was successful. Congratulations!',
                recipientProviders: [culprits()]
        }
        unstable {
            emailext subject: 'Build Unstable: ${currentBuild.fullDisplayName}',
                body: 'The build was unstable. Please investigate.',
                recipientProviders: [culprits()]
        }
        failure {
            emailext subject: 'Build Failure: ${currentBuild.fullDisplayName}',
                body: 'The build has failed. Please fix the issues.',
                recipientProviders: [culprits()]
        }
    }
}
