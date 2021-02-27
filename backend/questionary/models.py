import uuid
from django.db import models


# ======================
# Question
# ======================

class Question(models.Model):
    
    idQuestion = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    headQuestion = models.CharField(
        'Head Question',
        max_length=500
    )

    def get_choices(self):
        return ",".join([str(q) for q in self.choices.all()])

    def __str__(self):
        return self.headQuestion

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


# ======================
# Choice
# ======================

class Choice(models.Model):

    idChoice = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    textChoice = models.TextField(
        'Text Choice',
        max_length=200
    )

    question = models.ForeignKey(
        'Question',
        Question,
        verbose_name='question',
        related_name='choices'
    )

    score = models.FloatField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.textChoice

    class Meta:
        verbose_name = 'Choice'
        verbose_name_plural = 'Choices'


# ======================
# Questionary
# ======================

class Questionary(models.Model):
    
    idQuestionary = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(
        'Text name',
        max_length=250
    )

    questions = models.ManyToManyField(
        Question,
        verbose_name='questions',
        related_name='questionnaires'
    )

    def get_questions(self):
        return ",".join([str(q) for q in self.questions.all()])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Questionary'
        verbose_name_plural = 'Questionnaires'
