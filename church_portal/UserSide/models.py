from django.db import models
from accounts.models import Customusers
from AdminSide.models import sermon

# Create your models here.
class comment(models.Model):
    by = models.ForeignKey(Customusers, on_delete=models.CASCADE)
    cfor = models.ForeignKey(sermon,on_delete=models.CASCADE)
    content = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.by.username