from django.db import models

ESTADOS = [
    ('Borrador', 'Borrador'),
    ('Pendiente', 'Pendiente'),
    ('En proceso', 'En proceso'),
    ('Completada', 'Completada'),
]

PRIORIDADES = [
    (1, 'Baja'),
    (2, 'Media'),
    (3, 'Alta'),
]

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Borrador')
    fecha_creada = models.DateTimeField(auto_now_add=True)
    prioridad = models.IntegerField(choices=PRIORIDADES, default=1)
    fecha_limite = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo
    