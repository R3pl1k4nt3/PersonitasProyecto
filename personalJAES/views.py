from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import UnidadSerializer, DepartamentoSerializer, NegociadoSerializer, PersonaSerializer
from .models import Unidad, Departamento, Negociado, Persona

class UnidadViewSet(viewsets.ModelViewSet):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class NegociadoViewSet(viewsets.ModelViewSet):
    queryset = Negociado.objects.all()
    serializer_class = NegociadoSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
