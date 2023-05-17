from django.db import models
from django.contrib.auth.models import User
from datetime import date




from django.forms import BaseModelForm
# Create your models here.
class Produit(models.Model):
    catégorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, null=True)
    Membre = models.ForeignKey('Membre', on_delete=models.CASCADE, null=True)
    TYPE_CHOICES=[  ('em','emballé'),
                    ('fr','Frais'),
                    ('cs','Conserve')]
    libellé=models.CharField(max_length=100)
    description=models.TextField(default='non définie')
    prix=models.DecimalField(max_digits=10,decimal_places=3,default=0)
    qte = models.PositiveIntegerField(default=1)
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    img =models.ImageField(upload_to='media/', null=True, blank=True)
    
    def __str__(self):
        return self.libellé+","+self.description+","+str(self.prix)+","+self.type+","+str(self.qte)
    


class Categorie(models.Model):
    TYPE_CHOICES=[
    ('Al','Alimentaire'), ('Mb','Meuble'),
    ('Sn','Sanitaire'), ('Vs','Vaisselle'),
    ('Vt','Vêtement'),('Jx','Jouets'),
    ('Lg','Linge de Maison'),('Bj','Bijoux'),('Dc','Décor')
    ]

    name=models.CharField(max_length=50,default='Al',choices=TYPE_CHOICES)
    def __str__(self):
        return self.name
    
class Project(models.Model):
    titre=models.CharField(max_length=100,null=True)
    prix=models.DecimalField(max_digits=10,decimal_places=3,default=0)
    description = models.TextField(default="")
    logo =models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
         return (self.titre+','+self.description)


    
    
class Membre(models.Model):
    nom=models.CharField(max_length=100,null=True)
    adresse=models.CharField(max_length=100,null=True)
    email=models.EmailField(null=True)
    telephone=models.CharField(max_length=8,null=True)
    logo =models.ImageField(upload_to='media/', null=True, blank=True)
    def __str__(self):
        return (self.nom+','+self.adresse+','+self.email+','+self.telephone)
    


class Panier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Project, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class ProduitNC(Produit):
    Duree_garantie=models.CharField(max_length=100)
    
    def __str__(self):
        return "objet ProduitNC:%s"%(self.Duree_garantie)
