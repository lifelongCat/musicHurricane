from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompositionViewSet

router = DefaultRouter()
router.register(r'compositions', CompositionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
