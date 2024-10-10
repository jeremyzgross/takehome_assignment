from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import MemeTemplate

class MemeTemplateTest(APITestCase):
    """
    Test case for the MemeTemplate API.
    """

    def test_list_templates(self):
        """
        Test the API endpoint for listing all meme templates.
        """
        url = reverse('meme-template-list')  # Update to match the URL pattern name
        response = self.client.get(url)  # Make a GET request to the endpoint
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Assert that the response status is 200 OK