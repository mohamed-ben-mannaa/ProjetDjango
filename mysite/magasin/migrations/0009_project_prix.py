# Generated by Django 4.2 on 2023-05-16 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0008_rename_image_project_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='prix',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
    ]
