pipeline {
    agent any

    tools {
        jdk 'myjava'
        maven 'mymaven'
    }   
    parameters {
        string(name: 'ENV', defaultValue: 'Test', description: 'ENV to deploy')
        booleanParam(name: 'executeTests', defaultValue: true, description: 'decide to run the tests or not')
        choice(name: 'APPVERSION', choices: ['1.1', '1.2','1.3'], description: 'Choose the version')
    }
    stages {
        stage('Build')  {
            steps {
                echo "Build the code of the project ${params.APPVERSION}"
                
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
        stage('Deploy') {
            input {
                message "Provide the approval for prod"
                ok "Yes"
            }
            steps {
                echo 'Deploy the code to '
                
            }
        }
    }
    }
}
