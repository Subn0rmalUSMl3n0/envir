from django.db import models

class Comentario(models.Model):
    autor = models.CharField(max_length=100)
    ubicacion = models.CharField(help_text='(Favor pegar sin cambios desde el portapapeles)',max_length=140)
    contenido = models.CharField(max_length= 21381,help_text='Explique que ocurrió en su avistamiento')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.autor