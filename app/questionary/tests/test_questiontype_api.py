from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient


QUESTIONTYPES_URL = reverse('questionary:questiontype-list')


class PublicQuestionTypeTests(TestCase):
    """Test the publicly available question types API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login required for retrieving question types"""
        res = self.client.get(QUESTIONTYPES_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
