from django.db import models
from django.db.models.fields import IntegerField
from django.db.models.fields import CharField
from django.db.models.fields import DateField 

# Create your models here.
#class Tutorial(models.Model):
#    title = models.CharField(max_length=70, blank=False, default='')
#    description = models.CharField(max_length=200,blank=False, default='')
#    published = models.BooleanField(default=False)

class comentarios(models.Model):
    #id_comentario=models.IntegerField()
    id_producto=models.IntegerField()
    date_comment=models.DateTimeField(verbose_name='Fecha de creacion')
    rate_comment=models.IntegerField()
    comment=models.CharField(max_length=70, blank=False, default='')
    user=models.CharField(max_length=70)
    email_user=models.CharField(max_length=70)


class  pregunta(models.Model):
    #id_pregunta=models.IntegerField()
    date_pregunta=models.DateTimeField(verbose_name='Fecha de creacion')
    pregunta=models.CharField(max_length=70, blank=False, default='')
    user=models.CharField(max_length=70)
    email_user=models.CharField(max_length=70)

class calificaciones(models.Model):
    #id_calificacion=models.IntegerField()
    rate=models.IntegerField()
    id_producto=IntegerField()
    id_comprador=IntegerField()
