from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory, APITestCase
import time

from rest_framework.utils import json

from ..api import Video_statistics


class Teste_post(APITestCase):
    data = {
        "duration": "34.9",
        "timestamp": time.time()
    }

    def test_view_set(self):


        response = self.client.post(
            reverse('videos'),
            data=json.dumps(self.data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class Teste_Get(APITestCase):

    def test_get_valid_single_puppy(self):
        response = self.client.get(
            reverse('statistics'))



        self.assertEqual(response.status_code, status.HTTP_200_OK)



class Teste_Delete(APITestCase):

    def test_get_valid_single_puppy(self):
        response = self.client.delete(
            reverse('videos'))



        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)