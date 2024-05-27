from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Composition


class CompositionSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Composition
        fields = '__all__'
