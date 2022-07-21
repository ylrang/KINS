from django.db import models
from account.models import myUser


class Docs(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    regist_date = models.DateTimeField()
    last_updated = models.DateTimeField()
    writer = models.ForeignKey(myUser, on_delete=models.PROTECT)
    tags = models.ManyToManyField('kinsdb.Tag', related_name='tags')
    views = models.IntegerField(verbose_name='VIEWS', default=0)

    index_title = models.CharField(max_length=100, default='')
    index_num = models.FloatField(default=0)

    document = models.ForeignKey('kinsdb.Document', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Docs'
        verbose_name_plural = 'Docs'


class Tag(models.Model):
    tag_content = models.CharField(max_length=100)


def content_file_name(instance, filename):
    return '/'.join(['documents', instance.institution, filename])


class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to=content_file_name)
    serial_num = models.IntegerField(default=0, verbose_name='SERIAL')
    institution = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Documents'
        verbose_name_plural = 'Documents'
