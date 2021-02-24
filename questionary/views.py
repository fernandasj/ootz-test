from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from . import models
from . import serializers


# ======================
# Questionary
# ======================
class QuestionaryViewSet(viewsets.ModelViewSet):

    queryset = models.Questionary.objects.all()
    serializer_class = serializers.CreateQuestionarySerializer

    def create(self, request):
        new_questionary = models.Questionary.objects.create(name=request.data['name'])
        questions = request.data['questions']
        
        for question in questions:
            new_question = models.Question.objects.create(headQuestion=question['headQuestion'])
            new_questionary.questions.add(new_question)
            for choice in question['choices']:
                new_choice = models.Choice.objects.create(textChoice=choice['textChoice'], question_id=new_question.pk, score=choice['score'])

        new_questionary.save()
        return Response({'status': '200'})

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            return serializers.QuestionarySerializer
        return super().get_serializer_class()


class QuestionaryResultViewSet(viewsets.ModelViewSet):

    queryset = models.Choice.objects.all()

    def create(self, request):
        result = 0

        for choice in request.data['choices']:
            answer_choice = self.queryset.get(pk=choice['choice_id'])
            result += answer_choice.score

        return Response({'scores': result})