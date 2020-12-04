from django.urls import path, include
from rest_framework.routers import DefaultRouter

from questionary import views


router = DefaultRouter()
router.register('quiztypes', views.QuizTypeViewSet)

app_name = 'questionary'

urlpatterns = [
    path('', include(router.urls))
]
