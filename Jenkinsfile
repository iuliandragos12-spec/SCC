/* Jenkins pipeline declarativ pentru curs_scc_441D_masini */
pipeline {
    agent none

    stages {
        stage('Build') {
            agent any
            steps {
                echo 'Pregatire mediu virtual si dependinte...'
                sh '''
                    pwd;
                    ls -l;
                    . ./activeaza_venv_jenkins
                '''
            }
        }

        stage('pylint - calitate cod') {
            agent any
            steps {
                sh '''
                    . ./activeaza_venv;
                    echo "\n\nVerificare app/lib/*.py cu pylint";
                    pylint --exit-zero app/lib/*.py;

                    echo "\n\nVerificare app/tests/*.py cu pylint";
                    pylint --exit-zero app/tests/*.py;

                    echo "\n\nVerificare masini.py cu pylint";
                    pylint --exit-zero masini.py;
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            agent any
            steps {
                echo 'Rulare unit-test-uri...'
                sh '''
                    . ./activeaza_venv;
                    pytest;
                '''
            }
        }

        stage('Deploy') {
            agent any
            steps {
                echo 'Containerizare manuala (vezi Dockerfile + dockerstart.sh).'
            }
        }
    }
}
