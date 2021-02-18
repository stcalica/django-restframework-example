from django.conf.urls import re_path, url, include
from django.urls import path
from rest_framework import routers
from .question import QuestionViewSet

router = routers.DefaultRouter()
router.register("polls", QuestionViewSet)
urlpatterns = router.urls
