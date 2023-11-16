from django.db import models

from django.db import models

class Comentario(models.Model):
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to='comentarios_fotos/', blank=True, null=True)
    def __str__(self):
        return self.autor
