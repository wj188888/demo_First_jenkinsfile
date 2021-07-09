pipeline {
    agent any

    stages {
        stage('pull code') {
            steps {
                 checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: '52400ef3-5081-4ccc-9f80-d28c8616cead', url: 'https://github.com/wj188888/demo_interface.git']]])
            }
        }
        stage('build code') {
            steps {
                 bat '''cd C:\\Python37Venv\\my_interface\\Scripts
                activate && cd C:\\Users\\admin\\.jenkins\\workspace\\my_demo_pipeline\\test_demo && pytest -vs test_post.py'''
            }
        }
    }
}