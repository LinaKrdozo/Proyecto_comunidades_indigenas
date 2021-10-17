from django.db   import models

producto_type = [
    (1, 'tejido'),
    (2, 'ceramica'),
    (3, 'joyeria'),
    (4, 'Orfebreria'),
    (5, 'tallado'),
]

class Tipo_producto(models.Model):
    id              = models.AutoField(primary_key=True)
    nombre_tipo_prod = models.IntegerField(choices = producto_type)

