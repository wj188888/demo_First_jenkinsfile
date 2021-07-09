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
        stage('Delete workspace') {
            steps {
                deleteDir()
            }
        }
    }
    post {
         failure {
	        script {
	            mail to: '2460665525@qq.com',
                    subject: "Running Pipeline: ${currentBuild.fullDisplayName}",
                    body: "${FILE,path='email.html'}"
	        }
	    }
	    success {
	        script {
	            mail to: '1973702576@qq.com',
                    subject: "Running Pipeline: ${currentBuild.fullDisplayName}",
                    body: "${FILE,path='email.html'}"
	        }
	    }

}