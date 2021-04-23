from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SaveImageViewSet
router = DefaultRouter()
router.register("image-save", SaveImageViewSet, basename="image-Save")
urlpatterns = [
    path("", include(router.urls)),
]
