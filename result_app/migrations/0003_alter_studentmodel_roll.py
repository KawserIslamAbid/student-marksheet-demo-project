# Generated by Django 5.0.1 on 2024-02-04 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result_app', '0002_studentmodel_roll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='roll',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]