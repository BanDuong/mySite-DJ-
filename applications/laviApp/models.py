from django.db import models
from django.utils import timezone

# Create your models here.

class LaviType(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    color = models.CharField(max_length=100,default="white")
    created_at = models.DateTimeField(timezone.now())

    class Meta:
        db_table = "Lavi"

    def __str__(self):
        return self.name