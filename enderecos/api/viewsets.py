from rest_framework.viewsets import ModelViewSet

from .serializers import EnderecoSerializer
from ..models import Endereco


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
