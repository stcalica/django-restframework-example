#serializer and queryset
from rest_framework import serializers
from my_api.polls.models.question import Question
from rest_framework import viewsets

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = ["id", "question_text", "pub_date"]

class QuestionViewSet(viewsets.ModelViewSet):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer
