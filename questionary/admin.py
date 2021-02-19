from django.contrib import admin
from .models import Questionary, Question, Choice


# =====================
# QuestionaryAdmin
# =====================
class QuestionaryAdmin(admin.ModelAdmin):
    list_display = ('idQuestionary', 'name', 'get_questions')

admin.site.register(Questionary, QuestionaryAdmin)


# ======================
# QuestionAdmin
# ======================
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('idQuestion', 'headQuestion', 'get_choices')

admin.site.register(Question, QuestionAdmin)


# ======================
# ChoiceAdmin
# ======================
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('idChoice', 'textChoice', 'question')

admin.site.register(Choice, ChoiceAdmin)
