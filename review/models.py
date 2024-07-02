from django.db import models
from django.utils import timezone
from authentication.models import User
from court_management.models import Court


# Definición del modelo de estado de reservacion
class Review(models.Model):
    rating = models.PositiveSmallIntegerField(choices=[
        (1, '1 - Very Bad'),
        (2, '2 - Bad'),
        (3, '3 - Average'),
        (4, '4 - Good'),
        (5, '5 - Excellent'),
    ], null=False)
    comment = models.TextField(blank=True)
    comment_datetime = models.DateTimeField(default=timezone.now, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    court = models.ForeignKey(Court, on_delete=models.CASCADE, null=False)
