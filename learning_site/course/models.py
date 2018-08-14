from django.db import models

class Course(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()


# Create your models here.
