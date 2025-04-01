pipeline {
    agent any

    parameters{
        string(name: 'ENV', defaultValue: 'DEV', description: 'Environment to deploy')
    }

    stages {
        stage('Build') {
            steps {
                echo 'Build the code'
            }
        }    
        stage('Test') {
            steps {
                echo 'Run the Test cases'
            }
        }
        stage('Package') {
            steps {
                echo 'Package the code'
            }
        }
    }
}
