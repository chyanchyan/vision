# Generated by Django 3.1.4 on 2021-01-28 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataWidget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True, unique=True)),
                ('js_name', models.CharField(max_length=1000, unique=True)),
                ('data_structure_model_name', models.CharField(max_length=50, null=True)),
                ('comments', models.TextField(blank=True, verbose_name='Page Content')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('permalink', models.CharField(max_length=12, unique=True)),
                ('update_date', models.DateTimeField(verbose_name='Last Updated')),
                ('bodytext', models.TextField(blank=True, verbose_name='Page Content')),
                ('widgets', models.ManyToManyField(blank=True, to='pages.DataWidget')),
            ],
        ),
    ]
