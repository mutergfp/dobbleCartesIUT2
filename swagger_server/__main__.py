#!/usr/bin/env python3

import connexion
from flask_cors import CORS
from .encoder import JSONEncoder


if __name__ == '__main__':
	app = connexion.App(__name__, specification_dir='./swagger/')
	app.app.json_encoder = JSONEncoder
	app.add_api('swagger.yaml', arguments={'title': 'Card generation API'})
	
	CORS(app.app)
	
	app.run(port=8080, threaded=True)
