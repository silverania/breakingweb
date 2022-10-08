# Generated by Django 4.0.1 on 2022-10-08 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_alter_tutorial_visite'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='photos',
            field=models.ImageField(blank=True, null=True, upload_to='media/tuorial/images/'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='visite',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
