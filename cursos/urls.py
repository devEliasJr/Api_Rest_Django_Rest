from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (AvaliacaoAPIView, AvaliacaoViewSet, AvaliacoesAPIView,
                    CursoAPIView, CursosAPIView, CursoViewSet, MyNewView,
                    MyNewViewSet)

"""
API V2 routes - router - view set
"""
router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)
router.register('my-new-view', MyNewViewSet)





"""
API V1 routes - urlpatterns (generics, API View)
"""

urlpatterns = [

    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
    path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='cursos_avaliacoes'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>', AvaliacaoAPIView.as_view(), name='cursos_avaliacao'),

    path('my-new-view/', MyNewView.as_view(), name='my-new-view'),

    


    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
]
