from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    texto = models.TextField(max_length=3000)  #Text field permite más texto
    publicado_el = models.DateField()
