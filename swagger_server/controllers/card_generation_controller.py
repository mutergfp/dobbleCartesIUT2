import connexion
from swagger_server.models.card import Card
from swagger_server.models.inline_response200 import InlineResponse200
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from fonctionsGlobales import getImages
from random import randrange
import random
import json
from flask import make_response

def initial_cards(nbplayers):
	"""
	Génére les cartes de départ en fonction du nombre de joueurs
	
	:param nbplayers: Nombre de joueurs actuellement en jeu
	:type nbplayers: int

	:rtype: InlineResponse200
	"""
	if nbplayers > 1:
		if nbplayers < 9:
			images = getImages()

			nbJoueurs = nbplayers
			cartes = 2*['']
			cartes[0] = 8*['']
			cartes[1] = nbJoueurs*['']
			for i in range(nbJoueurs): 
				cartes[1][i] = 8*['']

			for j in range(8):
				while True:
					c_aleatoire = randrange(len(images))
					if(images[c_aleatoire] not in cartes[0]):
						cartes[0][j] = images[c_aleatoire]
						break

			for j in range(nbJoueurs):
				cartes[1][j][0] = cartes[0][randrange(8)]
				for x in range(7):
					while True:
						c_aleatoire = randrange(len(images))
						if images[c_aleatoire] not in cartes[0]:
							if images[c_aleatoire] not in cartes[1][j]:
								cartes[1][j][x+1] = images[c_aleatoire]
								break

			for i in range(nbJoueurs):
				random.shuffle(cartes[1][i])
			
			cartesJson = {}
			cartesJson["middleCard"] = cartes[0]
			cartesJson["playersCards"] = cartes[1]
			return cartesJson 
	return make_response("Invalid number supplied", 400)


def middle_card(CurrentCards):
	"""
	Génére une nouvelle carte du millieu à partir des cartes actuelles des joueurs
	
	:param CurrentCards: Cartes actuelles des joueurs
	:type CurrentCards: list | bytes

	:rtype: Card
	"""
	images = getImages()

	carteMilieu = 8*['']
	
	cartesJoueurs = CurrentCards

	for i in range(len(cartesJoueurs)):
		while True:
			c_aleatoire = randrange(8)
			if cartesJoueurs[i][c_aleatoire] not in carteMilieu:
				estOk = True
				for j in range(len(cartesJoueurs)):
					if j is not i:
						if cartesJoueurs[i][c_aleatoire] in cartesJoueurs[j]:
							estOk = False
				if estOk:
					carteMilieu[i] = cartesJoueurs[i][c_aleatoire]
					break
	
	for i in range(8-len(cartesJoueurs)):
		while True:
			c_aleatoire = randrange(len(images))
			estOk = True
			for j in range(len(cartesJoueurs)):
				if images[c_aleatoire] in cartesJoueurs[j]:
					estOk= False
			if estOk:
				if images[c_aleatoire] not in carteMilieu:
					carteMilieu[i+len(cartesJoueurs)] = images[c_aleatoire]
					break

	random.shuffle(carteMilieu)
	
	return carteMilieu