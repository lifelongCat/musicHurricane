from rest_framework.viewsets import ModelViewSet
from .serializers import CompositionSerializer
from .models import Composition


class CompositionViewSet(ModelViewSet):
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer

