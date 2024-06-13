from django.db import models


# Definición del modelo del tipo de superficie de la cancha
class SurfaceType(models.Model):
    type = models.CharField(max_length=100, null=False)


# Definición del modelo del estado de la cancha
class CourtStatus(models.Model):
    status = models.CharField(max_length=100, null=False)


# Definición del modelo del tipo de cancha
class CourtType(models.Model):
    type = models.CharField(max_length=100, null=False)


# Definición del modelo de canchas
class Court(models.Model):
    name = models.CharField(max_length=100, null=False)
    code = models.CharField(max_length=50, null=False, unique=True)
    size = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=255, null=False)
    price_hour = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='uploads/', null=True)
    surface_type = models.ForeignKey(SurfaceType, on_delete=models.CASCADE)
    court_status = models.ForeignKey(CourtStatus, on_delete=models.CASCADE)
    court_type = models.ForeignKey(CourtType, on_delete=models.CASCADE)


# Definición del modelo de imagenes de las canchas
class CourtImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    court = models.ForeignKey(Court, related_name='images', on_delete=models.CASCADE)
