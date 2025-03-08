from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FutureMessageViewSet

router = DefaultRouter()
router.register(r"future_messages", FutureMessageViewSet)

urlpatterns = [path("", include(router.urls))]
