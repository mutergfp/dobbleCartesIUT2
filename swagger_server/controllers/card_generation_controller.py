import connexion
from swagger_server.models.card import Card
from swagger_server.models.inline_response200 import InlineResponse200
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def initial_cards(nbplayers):
    """
    Génére les cartes de départ en fonction du nombre de joueurs
    
    :param nbplayers: Nombre de joueurs actuellement en jeu
    :type nbplayers: int

    :rtype: InlineResponse200
    """
    return 'do some magic!'


def middle_card(CurrentCards):
    """
    Génére une nouvelle carte du millieu à partir des cartes actuelles des joueurs
    
    :param CurrentCards: Cartes actuelles des joueurs
    :type CurrentCards: list | bytes

    :rtype: Card
    """
    if connexion.request.is_json:
        CurrentCards = [Card.from_dict(d) for d in connexion.request.get_json()]
    return 'do some magic!'
