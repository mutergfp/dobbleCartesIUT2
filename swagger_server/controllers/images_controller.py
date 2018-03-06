import connexion
from swagger_server.models.card import Card
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_img(img):
    """
    Ajoute une image aux possibilités pour la génération des cartes
    
    :param img: image à ajouter
    :type img: werkzeug.datastructures.FileStorage

    :rtype: None
    """
    return 'do some magic!'


def get_images():
    """
    Retourne la liste de toutes les images
    

    :rtype: List[Card]
    """
    return 'do some magic!'


def get_img(id):
    """
    Retourne l&#39;image correspondante à un ID
    
    :param id: Id de l&#39;image à récupèrer
    :type id: int

    :rtype: file
    """
    return 'do some magic!'
