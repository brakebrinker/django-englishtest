from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import QuizType

from questionary.serializers import QuizTypeSerializer


QUIZTYPES_URL = reverse('questionary:quiztype-list')


class PublicQuizTypeApiTests(TestCase):
    """Test the publicly available quiz types API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login required for retrieving quiz types"""
        res = self.client.get(QUIZTYPES_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
