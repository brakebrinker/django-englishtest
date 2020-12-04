from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import QuizType

from questionary import serializers


class BaseQuestionaryAttrViewSet(viewsets.GenericViewSet,
                                 mixins.ListModelMixin):
    """Base viewset for user owned questionary attributes"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """Create a new object"""
        serializer.save(user=self.request.user)


class QuizTypeViewSet(BaseQuestionaryAttrViewSet):
    """Manage quiztype in database"""
    queryset = QuizType.objects.all()
    serializer_class = serializers.QuizTypeSerializer
