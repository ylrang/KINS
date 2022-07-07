from django.db import models
from account.models import myUser


class Docs(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    regist_date = models.DateTimeField()
    last_updated = models.DateTimeField()
    writer = models.ForeignKey(myUser, on_delete=models.PROTECT)
    tags = models.ManyToManyField('kinsdb.Tag', related_name='tags')

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

#
class Tag(models.Model):
    tag_content = models.CharField(max_length=100)
