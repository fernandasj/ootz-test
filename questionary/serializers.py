from rest_framework import serializers
from . import models


# ======================
# Choice
# ======================
class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Choice
        fields = ('idChoice', 'textChoice', 'question', 'score')


class CreateChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Choice
        fields = ('idChoice', 'textChoice', 'question', 'score')
        list_serializer_class = ChoiceSerializer


# ======================
# Question
# ======================
class QuestionSerializer(serializers.ModelSerializer):

    choices = ChoiceSerializer(many=True)

    class Meta:
        model = models.Question
        fields = ('idQuestion', 'headQuestion', 'choices')
       

class CreateQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Question
        fields = ('idQuestion', 'headQuestion', 'choices')


# ======================
# Test
# ======================
class QuestionarySerializer(serializers.ModelSerializer):

    questions = QuestionSerializer(many=True)

    class Meta:
        model = models.Questionary
        fields = ('idQuestionary', 'name', 'questions')


class CreateQuestionarySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Questionary
        fields = ('idQuestionary', 'name', 'questions')
