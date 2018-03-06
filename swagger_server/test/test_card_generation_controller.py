# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.card import Card
from swagger_server.models.inline_response200 import InlineResponse200
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestCardGenerationController(BaseTestCase):
    """ CardGenerationController integration test stubs """

    def test_initial_cards(self):
        """
        Test case for initial_cards

        Génére les cartes de départ en fonction du nombre de joueurs
        """
        response = self.client.open('//cartes/{nbplayers}'.format(nbplayers=789),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_middle_card(self):
        """
        Test case for middle_card

        Génére une nouvelle carte du millieu à partir des cartes actuelles des joueurs
        """
        CurrentCards = [Card()]
        response = self.client.open('//carte',
                                    method='POST',
                                    data=json.dumps(CurrentCards),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
