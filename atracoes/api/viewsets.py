from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import AtracaoSerializer
from ..models import Atracao


class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao')

