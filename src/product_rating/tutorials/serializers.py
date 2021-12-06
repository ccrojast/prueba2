from rest_framework import serializers 
from tutorials.models import comentarios, pregunta, calificaciones
 
 
#class TutorialSerializer(serializers.ModelSerializer):
 
#    class Meta:
#        model = Tutorial
#        fields = ('id',
#                  'title',
#                  'description',
#                  'published',
#                  'comentarios')

class comentarioSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = comentarios
        fields = (
                  'id_producto',
                  'date_comment',
                  'rate_comment',
                  'comment',
                  'user',
                  'email_user')

class preguntaSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = pregunta
        fields = (
                  'date_pregunta',
                  'pregunta',
                  'user',
                  'email_user')

class calificacionSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = calificaciones
        fields = (
                  'rate',
                  'id_producto',
                  'id_comprador')