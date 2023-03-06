# Generated by Django 3.2.8 on 2023-03-06 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kinsdb', '0028_issue_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='report',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue', to='kinsdb.report'),
        ),
    ]
