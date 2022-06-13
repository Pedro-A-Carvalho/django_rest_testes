from rest_framework.serializers import ModelSerializer
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from core.models import PontoTuristico


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'foto', 'endereco', 'atracoes')

