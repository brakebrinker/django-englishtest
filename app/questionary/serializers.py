from rest_framework import serializers

from core.models import QuizType


class QuizTypeSerializer(serializers.ModelSerializer):
    """Serializer for quiztype objects"""

    class Meta:
        model = QuizType
        fields = ('id', 'name')
        read_only_fields = ('id',)



