from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import AbstractUser



class myUser(AbstractUser):
    COMPANY_CHOICES = (
        ('NCS', 'NC Square'),
        ('BRNC', 'brnc'),
        ('UNIST', 'unist'),
        ('KINS', 'kins'),
    )
    grade = models.CharField(default='A', max_length=100)
    writings = models.IntegerField(default=0)
    company = models.CharField(max_length=100, choices=COMPANY_CHOICES)


# class Folders(models.Model):
#     owner = models.ForeignKey(myUser, verbose_name="OWNER", on_delete=models.CASCADE, null=True)
#     title = models.TextField('TITLE', default='')
#     post_list = models.ManyToManyField('pages.Post')
#     created_at = models.DateTimeField('CREATED_AT', default=timezone.now)
#
#     class Meta:
#         verbose_name = 'folder'
#         verbose_name_plural = 'folders'
#
#
# # class UserFolder(models.Model):
#     myuser = models.ForeignKey(myUser, on_delete=models.CASCADE)
#     folder = models.ForeignKey(Folders, on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = 'User ManyToMany Table Folder'
