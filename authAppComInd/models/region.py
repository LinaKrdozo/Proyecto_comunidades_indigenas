from django.db import models

region_type = [
    (1, 'Caribe'),
    (2, 'Andina'),
    (3, 'Pacifico'),
    (4, 'Orinoquina'),
    (5, 'Amazonia'),
    (6, 'Insular'),
]

class Region(models.Model):
    id           = models.AutoField(primary_key=True)
    nombreRegion = models.IntegerField(choices = region_type)
