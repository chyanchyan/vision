# Generated by Django 3.1.4 on 2021-01-24 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datawidget',
            name='class_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]