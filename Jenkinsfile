pipeline {
  agent any
  options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
  }
  environment {
    DOCKERHUB_CREDENTIALS = credentials('ssah-blr-docker')
  }
  stages {
    stage('Build') {
      steps {
        dir('scripts') {
          sh """
          #!/bin/sh
          pwd
          ls -lrt
          cat Dockerfile
          docker build -t ssahblr/app2 .
          """
        }
      }
    }  
    stage('Login') {
      steps {
        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
      }
    }
    stage('Push') {
      steps {
        sh 'docker push ssahblr/app2'
      }
    }
  }
  post {
    always {
      sh 'docker logout'
    }
  }
}