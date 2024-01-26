from django.db import models
from account.models import myUser

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    charge = models.ForeignKey(myUser, on_delete=models.PROTECT, related_name='charge')
    participants = models.ManyToManyField(myUser)

    class Meta:
        verbose_name = 'Scheduling'
        verbose_name_plural = 'Scheduling'

    def __str__(self):
        return self.title



class Person(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=12, null=True)
    age = models.IntegerField(default=0)
    grade = models.FloatField(max_length=50, null=True)

    def __str__(self):
        return self.name

    objects = models.Manager()


class Log(models.Model):
    post = models.ForeignKey('cloud.Post', on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    description = models.TextField()
    # file_id = models.ForeignKey('cloud.Files', on_delete=models.CASCADE, related_name="log", db_column="file_id")


def log_file_name(instance, filename):
    return '/'.join(['posts', str(instance.log.post), str(instance.log), filename])


class Files(models.Model):
    file = models.FileField(upload_to=log_file_name)
    log = models.ForeignKey('cloud.Log', on_delete=models.CASCADE, related_name='files')

    class Meta:
        verbose_name = 'Files'
        verbose_name_plural = 'Files'

class Folder(models.Model):
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    owner = models.ForeignKey('account.myUser', on_delete=models.CASCADE)

class Post(models.Model):
    SECTOR = (
        ('1', '기관 제출 공문'),
        ('2', '참여기관 공유'),
        ('3', '회의일정 및 전체자료'),
        ('4', '기타'),
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    title = models.TextField()
    description = models.TextField()
    writer = models.ForeignKey('account.myUser', on_delete=models.CASCADE)
    tel = models.CharField(max_length=100)
    sector = models.CharField(max_length=100, choices=SECTOR, default='기타')
    folder = models.ForeignKey('cloud.Folder', on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id) + ') ' + self.title


# from django.db import models
# from django.utils import timezone
# from django.urls import reverse
# from account.models import myUser, Folders
#
# class Post(models.Model):
#     category = models.TextField('CATEGORY', default='')
#     title = models.TextField('TITLE', default='')
#     department = models.TextField('DEPARTMENT', default='')
#     charge = models.TextField('CHARGE', default='')
#     files = models.FileField(upload_to="files/%Y/%m/%d", blank=True)
#     regist_date = models.DateTimeField('REGIST DATE', default=timezone.now)
#     views = models.IntegerField(verbose_name='VIEWS', default=0)
#     writer = models.ForeignKey(
#         myUser, verbose_name="WRITER", on_delete=models.CASCADE, null=True)
#
#     class Meta:
#         verbose_name = 'post'
#         verbose_name_plural = 'posts'
#         db_table = 'posts'
#         ordering = ('-regist_date',)
#         permissions = [
#             ('can_view', 'Can View Post')
#         ]
#
#     def __str__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         return reverse('main:bulletin_detail', args=[self.id])
#
#     def get_previous(self):
#         return self.get_previous_by_mod_date()
#
#     def get_next(self):
#         return self.get_next_by_mod_date()
#
#     def get_content(self):
#         return self.content
