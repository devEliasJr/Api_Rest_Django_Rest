from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Avaliacao, Curso
from .serializers import AvaliacaoSerializer, CursoSerializer


class CursoAPIView(APIView):
    """
    API de Cursos
    """
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, {"Code": "SUCCESSFULY_CREATED"}, status=status.HTTP_201_CREATED)

class AvaliacaoAPIView(APIView):
    """
    API de Cursos
    """
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializier = AvaliacaoSerializer(data=request.data)
        serializier.is_valid(raise_exception=True)
        serializier.save()
        return Response(serializier.data, status=status.HTTP_201_CREATED)
        
      