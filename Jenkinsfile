pipeline {
    agent any

    tools {
        jdk 'myjava'
        maven 'mymaven'
    }   
    stages {
        stage('Build')  {
            steps {
                echo 'Build the code of the project'
                
            }
        }    
        stage('Test') {
            steps {
                echo 'Run the Test cases '
                
            }
        }
        stage('Package') {
            steps {
                echo 'Package the code'
                
            }
        }
    }
}
