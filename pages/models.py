from django.db import models
from account.models import myUser

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    charge = models.ManyToManyField(myUser)

    class Meta:
        verbose_name = 'Scheduling'
        verbose_name_plural = 'Scheduling'

#
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
