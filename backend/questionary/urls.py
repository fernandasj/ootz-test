from rest_framework import routers
from . import views as api

app_name = 'questionnaires-api'

router = routers.DefaultRouter()
router.register(r'questionnaries', api.QuestionaryViewSet)
router.register(r'result', api.QuestionaryResultViewSet)

urlpatterns = router.urls