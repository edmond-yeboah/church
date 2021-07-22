from django.db import models

# Create your models here.

class sermon(models.Model):
    title = models.CharField(blank=True, null=True, max_length=50)
    content = models.CharField(blank=True,null=True, max_length=5000)
    image = models.ImageField(upload_to='sermon_images')
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title