import connexion
from swagger_server.models.card import Card
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from fonctionsGlobales import getImages
import sqlite3
import glob
from flask import make_response
import imghdr
from PIL import Image

def add_img(img):
	"""
	Ajoute une image aux possibilités pour la génération des cartes
	
	:param img: image à ajouter
	:type img: werkzeug.datastructures.FileStorage

	:rtype: None
	"""
	if imghdr.what(img) is 'png':
		conn = sqlite3.connect('DobbleImages.sqlite')
		ablob = img.read()
		sql = '''INSERT INTO IMAGES
		(IMAGE)
		VALUES(?);'''
		conn.execute(sql,[sqlite3.Binary(ablob)])
		conn.commit()
		return 'successful operation'
	else:
		return make_response("Invalid image supplied", 400)


def get_images():
	"""
	Retourne la liste de toutes les images
	

	:rtype: List[Card]
	"""	
	return getImages()


def get_img(id):
	"""
	Retourne l&#39;image correspondante à un ID
	
	:param id: Id de l&#39;image à récupèrer
	:type id: int

	:rtype: file
	"""
	conn = sqlite3.connect('DobbleImages.sqlite')
	
	sql = "SELECT COUNT(*) FROM IMAGES"
	cursor = conn.cursor()
	cursor.execute(sql)	
	res = cursor.fetchone()
	if res[0] < id:
		return make_response("Invalid id supplied", 400)
	else:
		sql = "SELECT IMAGE FROM IMAGES WHERE ID = " + str(id)
		cursor = conn.cursor()
		cursor.execute(sql)	
		res = cursor.fetchone()
		if res[0]:
			img = res[0]
			img = img.resize((200,200), Image.ANTIALIAS)
			return img
		else: 
			return make_response("Invalid id supplied", 400)