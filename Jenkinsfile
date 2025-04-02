pipeline {
    agent none

    tools {
        jdk 'myjava'
        maven 'mymaven'
    }   
    stages {
        stage('Build')  {
            steps {
                echo 'Build the code'
                sh 'mvn compile'
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
