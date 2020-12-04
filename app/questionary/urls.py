from django.urls import path, include
from rest_framework.routers import DefaultRouter

from questionary import views


router = DefaultRouter()
router.register('quiz-types', views.QuizTypeViewSet)
router.register('question-types', views.QuestionTypeViewSet)

app_name = 'questionary'

urlpatterns = [
    path('', include(router.urls))
]
