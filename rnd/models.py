from django.db import models

# Create your models here.
    
def case_file_name(instance, filename):
    return '/'.join(['cases', instance.organization, filename])

class Regulation(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    description = models.TextField()
    writer = models.CharField(max_length=100)
    file = models.FileField()


    def __str__(self):
        return str(self.id) + ') ' + self.title

class Case(models.Model):
    ORG = (
        ('kaeri', 'KAERI'),
        ('korad', 'KORAD'),
    )
    STATUS = (
        ('검토중', '검토중'),
        ('완료', '완료'),
    )
    creation_date = models.DateTimeField()
    title = models.TextField(default="1차 보고서")
    update_date = models.DateTimeField(auto_now=True)
    organization = models.CharField(max_length=100, choices=ORG, default='KAERI')
    summary = models.TextField()
    file = models.FileField(upload_to=case_file_name)
    writer = models.CharField(max_length=100)
    status = models.CharField(max_length=3, choices=STATUS)
