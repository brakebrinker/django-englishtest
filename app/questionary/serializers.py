from rest_framework import serializers

from core.models import QuizType, QuestionType


class QuizTypeSerializer(serializers.ModelSerializer):
    """Serializer for quiztype objects"""

    class Meta:
        model = QuizType
        fields = ('id', 'name')
        read_only_fields = ('id',)


class QuestionTypeSerializer(serializers.ModelSerializer):
    """Serializer for questiontype abjects"""

    class Meta:
        model = QuestionType
        fields = ('id', 'name')
        read_only = ('id',)
