pipeline {
    agent any
    stages {
        stage('SCM') {
            steps {
                checkout([$class: 'GitSCM', 
                          branches: [[name: '*/main']], 
                          extensions: [],
                          userRemoteConfigs: [[credentialsId: 'github', url: 'https://github.com/devopsjayantBhagat/django.git']]])
            }
        }
        stage('build && SonarQube analysis') {
            steps {
			  def scannerHome = tool 'SonarQubeScanner'
              withSonarQubeEnv('SonarQube') {
                  sh "ls ${scannerHome}"
                  sh "echo ${scannerHome}"
                }
            }
        }
        stage("Quality Gate") {
            steps {
                timeout(time: 1, unit: 'HOURS') {
                    // Parameter indicates whether to set pipeline to UNSTABLE if Quality Gate fails
                    // true = set pipeline to UNSTABLE, false = don't
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }

}
