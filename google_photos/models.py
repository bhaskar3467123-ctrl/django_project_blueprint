from django.db import models

# Create your models here.
class Userphoto(models.Model):
    title=models.CharField(max_length=100, blank=True)
    description=models.TextField(blank=True, null=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title