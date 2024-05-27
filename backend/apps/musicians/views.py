from rest_framework.viewsets import ModelViewSet

from .models import Composition
from .serializers import CompositionSerializer


class CompositionViewSet(ModelViewSet):
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer
