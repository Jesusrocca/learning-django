from rest_framework import serializers
from inmuebleslist_app.models import Inmueble

#funcion que se encarga de validar la propiedad direccion
def column_longitud(value):
   if len(value) < 2:
      raise serializers.ValidationError('El valor es demasiado corto')

   
class InmuebleSerializer(serializers.Serializer):
   id=serializers.IntegerField(read_only=True)
   direccion = serializers.CharField(validators=[column_longitud])
   pais = serializers.CharField(validators=[column_longitud])   
   description = serializers.CharField()
   imagen = serializers.CharField()
   active = serializers.BooleanField()
   
   def create(self, validated_data):
      return Inmueble.objects.create(**validated_data)
   
   def update(self, instance, validated_data):
      print("Instance:", instance)
      print("Validated Data:", validated_data)
      instance.direccion = validated_data.get('direccion', instance.direccion)
      instance.pais = validated_data.get('pais', instance.pais)
      instance.description = validated_data.get('description', instance.description)
      instance.imagen = validated_data.get('imagen', instance.imagen)
      instance.active = validated_data.get('active', instance.active)
      instance.save()
      return instance
   
def validate(self, data):
    if data['direccion'] == data['pais']:
        raise serializers.ValidationError("La dirección y el país deben ser diferentes")
    else:
        return data

   
'''
   
from rest_framework import serializers
from inmuebleslist_app.models import Inmueble

class InmuebleSerializer(serializers.Serializer):
   id = serializers.IntegerField(read_only=True)
   direccion = serializers.CharField()
   pais = serializers.CharField()
   descripcion = serializers.CharField()
   imagen = serializers.CharField()
   active = serializers.BooleanField()
   
   def create(self, validated_data):
      return Inmueble.objects.create(**validated_data)
   
   def update(self, instance, validated_data):
      instance.direccion = validated_data.get('direccion', instance.direccion)
      instance.pais = validated_data.get('pais', instance.pais)
      instance.descripcion = validated_data.get('descripcion', instance.descripcion)
      instance.imagen = validated_data.get('imagen', instance.imagen)
      instance.active = validated_data.get('active', instance.active)
      instance.save()
      return instance
'''