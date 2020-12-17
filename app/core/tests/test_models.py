from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@englishtes.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


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

    def test_questiontype_str(self):
        """Test the questiontype string representation"""
        questiontype = models.QuestionType.objects.create(
            name='Multiple'
        )

        self.assertEqual(str(questiontype), questiontype.name)

    def test_question_str(self):
        """Test the question string representation"""
        question_type = models.QuestionType.objects.create(name='Match')
        question = models.Question.objects.create(
            user=sample_user(),
            title='Match cases',
            description='Try to match the following phrases',
            scores=4,
            duration_minutes=5,
            type=question_type
        )

        self.assertEqual(str(question), question.title)

    def test_quiz_str(self):
        """Test the quiz string representation"""
        user = sample_user()
        quiz = models.Quiz.objects.create(
            title='Level up test quiz',
            description='To up your level you should pass the test',
            published=True,
            created_by=user,
            modified_by=user
        )

        self.assertEqual(str(quiz), quiz.title)

    def test_answer_str(self):
        """Test the answer string representation"""
        question_type = models.QuestionType.objects.create(name='Word order')
        question = models.Question.objects.create(
            user=sample_user(),
            title='Word order',
            description='Try to make correct word order',
            scores=4,
            duration_minutes=5,
            type=question_type
        )
        answer = models.Answer.objects.create(
            initial='Word order wrong',
            target='Wrong word order',
            question=question
        )

        self.assertEqual(str(answer), answer.target)
