from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CompositionViewSet

router = DefaultRouter()
router.register('compositions', CompositionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
