from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CompositionViewSet, DownloadComposition

router = DefaultRouter()
router.register('compositions', CompositionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('download/<composition_id>/', DownloadComposition.as_view()),
]
