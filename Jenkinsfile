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
                withSonarQubeEnv('SonarQube') {
                    sh "/var/jenkins_home/tools/hudson.plugins.sonar.SonarRunnerInstallation/sonarqubescanner/bin/sonar-scanner -Dsonar.host.url=http://192.168.0.107:9000 -Dsonar.projectName=testing -Dsonar.projectVersion=1.0 -Dsonar.projectKey=meanstack:app -Dsonar.sources=. -Dsonar.projectBaseDir=/var/jenkins_home/workspace/testing"
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
