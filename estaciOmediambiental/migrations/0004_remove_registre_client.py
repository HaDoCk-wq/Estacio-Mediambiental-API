# Generated by Django 3.1.7 on 2021-02-23 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estaciOmediambiental', '0003_auto_20210223_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registre',
            name='client',
        ),
    ]
