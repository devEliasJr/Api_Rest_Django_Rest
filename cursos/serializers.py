from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import Avaliacao, Curso


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'avaliacao',
            'cricao',
            'ativo',
        )

    def validate_avaliacao(self, valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError('A avaliação deve ser um inteiro entre 1 e 5')

class CursoSerializer(serializers.ModelSerializer): 
    #Nested relationship
    #avaliacoes  = AvaliacaoSerializer(many=True, read_only=True)

    #Hyperlinked Related Field
    avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    #Primary  Key Related Field
    #avaliacoes  = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'cricao',
            'ativo',
            'avaliacoes'
        )

