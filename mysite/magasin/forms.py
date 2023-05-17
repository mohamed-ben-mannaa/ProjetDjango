from django import forms
from django.forms import ModelForm
from .models import Categorie, Produit
from .models import Membre, Project
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class ProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = "__all__"  # pour tous les champs de la table
        # fields=['libellé','description']  #pour qulques champs


class MembreForm(ModelForm):
    class Meta:
        model = Membre
        fields = "__all__"  # pour tous les champs de la table


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"


class CategorieForm(ModelForm):
    class Meta:
        model = Categorie
        fields = "__all__"  # pour tous les champs de la table


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + \
            ('first_name', 'last_name', 'email')
