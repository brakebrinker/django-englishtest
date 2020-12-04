from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful """
        email = 'test@englishtest.com'
        password = 'Test123456'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)

    def test_new_user_email_normalized(self):
        """ Test the email for a new user is normalized """
        email = 'test@ENGLISHTEST.com'
        user = get_user_model().objects.create_user(
            email=email,
            password='test124'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Test1234')

    def test_create_new_superuser(self):
        """ Test creating a new super user """
        user = get_user_model().objects.create_superuser(
            'test@englishtest.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_quiztype_str(self):
        """Test the quiztype string representation"""
        quiztype = models.QuizType.objects.create(
            name='Course'
        )

        self.assertEqual(str(quiztype), quiztype.name)
