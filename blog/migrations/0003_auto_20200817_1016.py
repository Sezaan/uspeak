# Generated by Django 3.0.9 on 2020-08-17 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='emails',
            new_name='email',
        ),
    ]
