from django.contrib import admin
from .models import Produit
from .models import Categorie
from .models import Membre
from .models import ProduitNC
from .models import Project

admin.site.register(ProduitNC)
admin.site.register(Project)
admin.site.register(Membre)
admin.site.register(Produit)
admin.site.register(Categorie)