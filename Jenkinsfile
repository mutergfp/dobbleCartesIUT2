node {
    def app
    stage('Clone repository') {
        /*Repo is cloned*/
        checkout scm
    }
    stage('Build image') {
        app = docker.build("gi1/dobble_cartes")
    }
	stage('Run image') {
		sh 'docker stop dobbleCartes'
		app.run('-p 82:8080 -it --rm --name dobbleCartes')
	}
}