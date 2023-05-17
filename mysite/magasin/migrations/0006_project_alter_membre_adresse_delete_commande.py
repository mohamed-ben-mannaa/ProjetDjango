# Generated by Django 4.2 on 2023-05-15 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0005_rename_fournisseur_membre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.AlterField(
            model_name='membre',
            name='adresse',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Commande',
        ),
    ]