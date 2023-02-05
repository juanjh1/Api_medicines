from django.db import models
from laboratories.models import laboratory
# Create your models here.
class Medicines (models.Model):
    name = models.CharField(max_length=50, null=False)
    price= models.IntegerField(default=1, null=False)
    laboratory= models.ForeignKey(laboratory, on_delete= models.CASCADE, related_name='medicines')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name