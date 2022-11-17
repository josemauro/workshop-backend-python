from django.db import models


class Teacher(models.Model):
    """Model to represent a teacher."""
    name = models.CharField(max_length=100, null=False, blank=False)
    price_per_hour = models.DecimalField(max_digits=9, decimal_places=2,
                                         null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    picture = models.URLField(max_length=255, null=False, blank=False)
