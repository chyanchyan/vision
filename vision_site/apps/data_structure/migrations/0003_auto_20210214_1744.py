# Generated by Django 3.1.4 on 2021-02-14 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_structure', '0002_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='test',
            new_name='text',
        ),
    ]