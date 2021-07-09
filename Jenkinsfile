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
            emailext attachmentsPattern: 'email.html' //附件中携带测试报告
            attachLog: true, // 附件中携带构建LOG
            // 邮件内容
            body: '构建失败日志请参考附件',
            // 邮件接收人,culprits包含了近期提交人员和触发人员
            recipientProviders: [culprits()], subject: 'Jenkins构建通知 - $PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS!', to: '2460665525@qq.com, 1973702576@qq.com'
        }
}