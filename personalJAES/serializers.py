from rest_framework import serializers
from .models import *

class UnidadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unidad
        fields = ('unidad', 'id', 'url')

class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields = ('departamento', 'unidad' , 'id', 'url')
        
class NegociadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Negociado
        fields = ('negociado', 'departamento')

class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = ('id','url','empleo','nombre','apellidos','telefono','fecha_incorporacion','fotografia','unidad','departamento')