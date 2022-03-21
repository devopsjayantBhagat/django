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
		    environment {
        scannerHome = tool 'SonarQubeScanner'
                }
            steps {
			  withSonarQubeEnv('SonarQube') {
			      sh "${scannerHome}/bin/sonar-scanner"
                  sh "ls ${scannerHome}"
                  sh "echo ${scannerHome}"
                }
            }
        }
        stage("Quality Gate") {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    // Parameter indicates whether to set pipeline to UNSTABLE if Quality Gate fails
                    // true = set pipeline to UNSTABLE, false = don't
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }

}
