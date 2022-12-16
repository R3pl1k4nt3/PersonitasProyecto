from rest_framework import serializers
from .models import *

class UnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = ('unidad',)

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ('departamento', 'unidad')
        
class NegociadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Negociado
        fields = ('negociado', 'departamento')

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('empleo','nombre','apellidos','telefono','fecha_incorporacion','fotografia','unidad','departamento')