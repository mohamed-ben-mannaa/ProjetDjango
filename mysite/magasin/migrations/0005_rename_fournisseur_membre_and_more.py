# Generated by Django 4.2 on 2023-05-15 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0004_rename_categorie_produit_catégorie_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fournisseur',
            new_name='Membre',
        ),
        migrations.RenameField(
            model_name='produit',
            old_name='fournisseur',
            new_name='Membre',
        ),
    ]