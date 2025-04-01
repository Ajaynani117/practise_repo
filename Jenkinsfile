pipeline {
    agent any

    tools {
        jdk 'myjava'
        maven 'mymaven'
    }

    environment{
        javaHome = '/usr/lib/jvm/java-8-openjdk-amd64'
        mvnHome = '/opt/apache-maven-3.6.3'
        dockerHome = '/usr/bin/docker'
    }
   

    stages {
        stage('Build')  {
            steps {
                echo 'Build the code'
                sh 'mvn package'
            }
        }    
        stage('Test') {
            steps {
                echo 'Run the Test cases '
                sh 'mvn test'
            }
        }
        stage('Package') {
            steps {
                echo 'Package the code'
                sh 'mvn package'
            }
        }
    }
}
