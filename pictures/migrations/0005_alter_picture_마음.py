# Generated by Django 4.2.9 on 2024-02-01 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0004_alter_mind_options_alter_mind_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='마음',
            field=models.ManyToManyField(blank=True, null=True, related_name='mind', to='pictures.mind'),
        ),
    ]
