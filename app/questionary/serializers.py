from rest_framework import serializers

from core.models import QuizType, QuestionType, Quiz


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
        read_only_fields = ('id',)


class QuizSerializer(serializers.ModelSerializer):
    """Serializer for quiz objects"""

    class Meta:
        model = Quiz
        fields = (
            'id',
            'title',
            'description',
            'published',
            'created_at',
            'modified_at',
            'created_by',
            'modified_by'
        )
        read_only_fields = ('id',)
