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

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag_content = models.CharField(max_length=100)

    def __str__(self):
        return self.tag_content



def content_file_name(instance, filename):
    return '/'.join(['documents', instance.institution, filename])


class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to=content_file_name)
    serial_num = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Documents'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.title


class Site(models.Model):
    title = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    factor = models.CharField(max_length=100)
    keywords = models.ManyToManyField('kinsdb.Keyword', related_name='keywords')
    preference = models.TextField(blank=True)
    description = models.TextField(blank=True)

    regist_date = models.DateTimeField()
    last_updated = models.DateTimeField()
    writer = models.ForeignKey(myUser, on_delete=models.PROTECT)


class Keyword(models.Model):
    key_content = models.CharField(max_length=100)

    def __str__(self):
        return self.key_content


####
