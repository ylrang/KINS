from django.db import models

# Create your models here.
class Regulation(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    description = models.TextField()
    writer = models.CharField(max_length=100)
    file = models.FileField()

    def __str__(self):
        return str(self.id) + ') ' + self.title
