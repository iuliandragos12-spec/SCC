/* Jenkins pipeline declarativ pentru curs_scc_441D_masini (Citroen C5 X)
 *
 * Etape:
 *   Build                  -> creeaza venv-ul si instaleaza dependintele
 *   pylint - calitate cod  -> analiza statica a codului
 *   Unit Testing cu pytest -> ruleaza testele unitare
 *   Build image            -> construieste imaginea Docker (foloseste Dockerfile)
 *   Deploy                 -> opreste containerul vechi si porneste unul nou pe 5011
 *
 * Necesita pe agentul Jenkins: python3, python3-venv si docker, iar user-ul
 * 'jenkins' trebuie sa fie in grupul 'docker' (altfel "docker build" da
 * permission denied pe /var/run/docker.sock).
 */
pipeline {
    agent any

    environment {
        IMAGE     = "curs_scc_441d_masini"
        TAG       = "dev"
        CONTAINER = "masini_c5"
        HOST_PORT = "5011"
        CONT_PORT = "5011"
    }

    stages {
        stage('Build') {
            steps {
                echo 'Pregatire mediu virtual si dependinte...'
                sh '''
                    pwd
                    ls -l
                    . ./activeaza_venv_jenkins
                '''
            }
        }

        stage('pylint - calitate cod') {
            steps {
                sh '''
                    . ./activeaza_venv

                    echo "\n\nVerificare app/lib/*.py cu pylint"
                    pylint --exit-zero app/lib/*.py

                    echo "\n\nVerificare app/tests/*.py cu pylint"
                    pylint --exit-zero app/tests/*.py

                    echo "\n\nVerificare masini.py cu pylint"
                    pylint --exit-zero masini.py
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            steps {
                echo 'Rulare unit-test-uri...'
                sh '''
                    . ./activeaza_venv
                    pytest
                '''
            }
        }

        stage('Build image') {
            steps {
                echo 'Construire imagine Docker...'
                sh '''
                    docker build -t ${IMAGE}:${TAG} .
                    docker images | grep ${IMAGE} || true
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Pornire container pe portul 5011...'
                sh '''
                    docker stop ${CONTAINER} || true
                    docker rm ${CONTAINER} || true
                    docker run -d -p ${HOST_PORT}:${CONT_PORT} \
                        --name ${CONTAINER} ${IMAGE}:${TAG}
                    docker ps
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline OK. Aplicatia ruleaza pe http://localhost:5011/'
        }
        failure {
            echo 'Pipeline a esuat. Verifica log-ul stage-ului care a picat.'
        }
    }
}
