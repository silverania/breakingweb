# Generated by Django 4.0.1 on 2022-09-21 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Visite',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='visite',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
