from rest_framework import serializers
from .models import *

class UnidadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unidad
        fields = ('unidad',)

class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields = ('departamento', 'unidad')
        
class NegociadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Negociado
        fields = ('negociado', 'departamento')

class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = ('empleo','nombre','apellidos','telefono','fecha_incorporacion','fotografia','unidad','departamento')