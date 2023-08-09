from django.db import models
from account.models import myUser


# class DocTest(models.Model):
#     title = models.CharField(max_length=200)  # 제목
#
#     # field = models.ForeignKey('kinsdb.Field', on_delete=models.SET_NULL, null=True)    #작성자
#     index_num = models.FloatField(default=0)  # 항목번호
#     index_title_eng = models.CharField(max_length=100, default='')  # 목차
#     index_title_kor = models.CharField(max_length=100, default='')  # 목차
#
#     sector = models.CharField(max_length=40, default='-')
#
#     content_kor = models.TextField()  # 상세내용
#     content_eng = models.TextField()
#
#     views = models.IntegerField(verbose_name='VIEWS', default=0)  # 조회
#     regist_date = models.DateTimeField(auto_now_add=True, blank=True)  # 등록일자
#     last_updated = models.DateTimeField(
#         auto_now_add=True, blank=True)  # 최근 수정일
#
#
#     writer = models.ForeignKey(myUser, on_delete=models.PROTECT)  # 작성자
#     tags = models.ManyToManyField(
#         'kinsdb.Tag', related_name='tags', blank=True)  # 태그
#
#     document = models.ForeignKey(
#         'kinsdb.Document', on_delete=models.CASCADE)  # 문서     #국가 포함
#


# class Test(models.Model):
#     # id = models.AutoField(primary_key=True)
#
#     no = models.CharField(max_length=100)
#     constitution = models.CharField(max_length=100)
#     index_no = models.CharField(max_length=10)
#     category = models.CharField(max_length=100)
#     content = models.TextField(default='')
#
#     def __str__(self):
#         return '[' + self.no + '] ' + self.index_no
#
#     class Meta:
#         db_table = 'Test'
#
#         constraints = [
#             models.UniqueConstraint(
#                 fields=["no", "index_no"],
#                 name="unique doc",
#             )
#         ]


class Docs(models.Model):
    title = models.CharField(max_length=200)  # 제목
    content_kor = models.TextField()  # 상세내용
    content_eng = models.TextField()
    # field = models.ForeignKey('kinsdb.Field', on_delete=models.SET_NULL, null=True)    #작성자

    regist_date = models.DateTimeField(auto_now_add=True, blank=True)  # 등록일자
    last_updated = models.DateTimeField(
        auto_now_add=True, blank=True)  # 최근 수정일
    writer = models.ForeignKey(myUser, on_delete=models.PROTECT)  # 작성자
    tags = models.ManyToManyField(
        'kinsdb.Tag', related_name='tags', blank=True)  # 태그
    views = models.IntegerField(verbose_name='VIEWS', default=0)  # 조회

    index_title_kor = models.CharField(max_length=100, default='')  # 목차
    index_num = models.CharField(max_length=100)  # 항목번호

    index_title_eng = models.CharField(max_length=100, default='')  # 목차

    sector = models.CharField(max_length=40, default='-')

    document = models.ForeignKey(
        'kinsdb.Document', on_delete=models.CASCADE)  # 문서     #국가 포함

    wc = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Docs'
        verbose_name_plural = 'Docs'

        constraints = [
            models.UniqueConstraint(
                fields=["document", "index_num"],
                name="unique document",
            )
        ]

    def __str__(self):
        return str(self.index_num) + ') ' + self.title


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
        verbose_name = 'BRNC_Documents'
        verbose_name_plural = 'BRNC_Documents'

    def __str__(self):
        return str(self.id) + ') ' + self.serial_num

from django.utils import timezone
def data_file_name(instance, filename):
    time = timezone.now().strftime('%y%m%d%H%M%S')
    bar = '_'
    return '/'.join(['data', filename + '_' + time ])



class Data(models.Model):
    document = models.ForeignKey(
        'kinsdb.Document', on_delete=models.CASCADE)
    file = models.FileField(upload_to=data_file_name)
    last_updated = models.DateTimeField(auto_now_add=True, blank=True)




class Report(models.Model):
    title = models.CharField(max_length=200)
    serial_num = models.IntegerField()
    background = models.TextField(blank=True)
    image = models.ImageField(upload_to='kinsdb', blank=True, null=True)

    class Meta:
        verbose_name = 'UNIST_Reports'
        verbose_name_plural = 'UNIST_Reports'

    def __str__(self):
        return self.title


class Issue(models.Model):
    issue = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    report = models.ForeignKey(
        Report, on_delete=models.CASCADE, related_name='issue')

    def __str__(self):
        return self.issue


class Site(models.Model):
    title = models.CharField(max_length=200)
    country = models.CharField(max_length=100)

    category = models.CharField(max_length=100)
    group = models.CharField(max_length=100)

    # factor = models.ForeignKey('kinsdb.Factor', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class SWFactor(models.Model):
    title = models.CharField(max_length=200)

    factor = models.CharField(max_length=100)

    requirement = models.TextField(blank=True)
    preference = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Keyword(models.Model):
    key_content = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.key_content


# class Field(models.Model):
#     field = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.field


####
