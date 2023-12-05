from django.db import models

class Inf_animales(models.Model):
    id_inf = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    habitad = models.CharField(max_length=100)
    estado_conservacion = models.CharField(max_length=300)
    informacion = models.CharField(max_length=500)
    imagen = models.CharField(max_length=300)
    created_by_2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inf_animales'
        
    using = 'mysql'

# Create your models here.
