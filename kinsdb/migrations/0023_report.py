# Generated by Django 3.2.8 on 2023-03-03 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinsdb', '0022_alter_document_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('serial_num', models.IntegerField()),
            ],
            options={
                'verbose_name': 'UNIST_Reports',
                'verbose_name_plural': 'UNIST_Reports',
            },
        ),
    ]