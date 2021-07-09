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
        always {
        // One or more steps need to be included within each condition's block.
            emailext body: '亲爱的同学们，Jenkins的使用爱好者，如果你们有收到这个邮件，代表Jenkins邮件发送成功，谢谢大家的配合~', recipientProviders: [brokenBuildSuspects()], subject: '【Jenkins构建结果测试】', to: '2460665525@qq.com'
        }
    }
}