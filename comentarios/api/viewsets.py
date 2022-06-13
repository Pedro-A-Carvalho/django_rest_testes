from rest_framework.viewsets import ModelViewSet

from .serializers import ComentarioSerializer
from ..models import Comentario


class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
