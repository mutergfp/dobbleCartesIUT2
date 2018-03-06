# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.card import Card
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestImagesController(BaseTestCase):
    """ ImagesController integration test stubs """

    def test_add_img(self):
        """
        Test case for add_img

        Ajoute une image aux possibilités pour la génération des cartes
        """
        data = dict(img=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open('//image',
                                    method='POST',
                                    data=data,
                                    content_type='multipart/form-data')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_images(self):
        """
        Test case for get_images

        Retourne la liste de toutes les images
        """
        response = self.client.open('//images',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_img(self):
        """
        Test case for get_img

        Retourne l'image correspondante à un ID
        """
        response = self.client.open('//image/{id}'.format(id=789),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
