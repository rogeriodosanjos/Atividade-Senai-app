pipeline {
    agent any

    environment {
        versionApp = sh "grep -i docker project.conf | awk -F = '{print $2}'"
        versionImage = sh "grep -i image project.conf | awk -F = '{print $2}'"
        nameProject = sh "grep -i nameProject project.conf | awk -F = '{print $2}'"
        repoDocker = sh "grep -i repoDocker project.conf | awk -F = '{print $2}'"
    }

    stages {
        stage('Demo') {
            steps {
                echo ${repoDocker}
                echo ${nameProject}
            }
        }
    }
}

