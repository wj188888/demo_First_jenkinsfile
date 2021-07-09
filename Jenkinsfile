pipeline {
    agent any

    stages {
        stage('Pull code') {
            steps {
                 checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'd76e3fab-0b01-4340-8a77-947322ed4c93', url: 'git@github.com:wj188888/demo_interface.git']]])
            }
        }
        stage('Build code') {
            steps {
                 bat '''cd C:\\Python37Venv\\my_interface\\Scripts
                activate && cd C:\\Users\\admin\\.jenkins\\workspace\\my_demo_pipeline\\test_demo && pytest -vs test_post.py'''
            }
        }
    }
    post {
        always {
            emailext(
                subject: "[${env.JOB_NAME}] [${env.ENV}] #${env.BUILD_NUMBER} : ${currentBuild.currentResult}",
                body: '${FILE,path="email.html"}',
                attachLog: true,
                recipientProviders: [[$class: 'DevelopersRecipientProvider', $class: 'CulpritsRecipientProvider']],
                mimeType: 'text/html',
                to: '2460665525@qq.com, 1973702576@qq.com'
            )
            deleteDir()
        }
    }

}