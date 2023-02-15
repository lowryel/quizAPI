from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class QuizSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Quizzes
        fields = ['title', 'date_created', 'category']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'answer_text', 'is_right']

class RandomQuestionSerializer(serializers.ModelSerializer):
    answer=AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['title', 'answer']

class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ['quiz','title', 'answer']



