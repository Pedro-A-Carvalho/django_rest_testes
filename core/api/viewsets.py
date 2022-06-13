from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import PontoTuristicoSerializer
from core.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('nome', 'descricao')

    def get_queryset(self):
        return PontoTuristico.objects.all()

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)
    #
    # def create(self, request, *args, **kwargs):
    #     pass
    # 
    # def destroy(self, request, *args, **kwargs):
    #     pass
    # 
    # def retrieve(self, request, *args, **kwargs):
    #     pass
    # 
    # def update(self, request, *args, **kwargs):
    #     pass

    @action(methods=['get'],detail=True)
    def teste(self, request, pk=None):
        pass
