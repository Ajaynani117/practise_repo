pipeline {
    agent any

    parameters{
        string(name: 'ENV', defaultValue: 'DEV', description: 'Environment to deploy')
        booleanParam(name: 'DEPLOY', defaultValue: true, description: 'Deploy the code')
        choice(name: 'CHOICE', choices: ['DEV', 'QA', 'PROD'], description: 'Choose the environment')
    }

    stages {
        stage('Build') {
            when {
                expression {
                    return params.DEPLOY == true
                }
            }
            steps {
                echo 'Build the code'
            }
        }    
        stage('Test') {
            steps {
                echo "Run the Test cases ${params.choices}"
            }
        }
        stage('Package') {
            steps {
                echo "Package the code env: ${params.ENV}"
            }
        }
    }
}
