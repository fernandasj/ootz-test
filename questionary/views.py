from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers


# ======================
# Questionary
# ======================
class QuestionaryViewSet(viewsets.ModelViewSet):

    queryset = models.Questionary.objects.all()
    serializer_class = serializers.CreateQuestionarySerializer

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            return serializers.QuestionarySerializer
        return super().get_serializer_class()