# Generated by Django 4.2.9 on 2024-02-01 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0005_alter_picture_마음'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mind',
            name='created',
        ),
        migrations.RemoveField(
            model_name='mind',
            name='updated',
        ),
    ]
