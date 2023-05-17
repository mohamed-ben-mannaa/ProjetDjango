from django.conf import settings
from django.shortcuts import redirect, render, get_object_or_404
from .models import Categorie, Panier, Produit
from .models import Membre, Project
from django.core.mail import send_mail
from .forms import ProduitForm, MembreForm, UserRegistrationForm, UserCreationForm, ProjectForm, CategorieForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.urls import reverse_lazy


def index(request):
    if request.method == "POST":
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            list = Produit.objects.all()
            return render(request, 'Produits/vitrineP.html', {'list': list})
    else:
        form = ProduitForm()  # créer formulaire vide
        list = Produit.objects.all()
        return render(request, 'Produits/create_product.html', {'form': form, 'list': list})

def edit_product(request, pk):
    product = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            # Récupérer l'instance du modèle produit
            produit = form.save(commit=False)
            # Récupérer la nouvelle image téléchargée
            nouvelle_image = form.cleaned_data['img']
            # Si une nouvelle image a été téléchargée, la sauvegarder
            if nouvelle_image:
                produit.img = nouvelle_image
            # Sauvegarder le produit
            produit.save()
            return redirect('Catalogue')
    else:
        form = ProduitForm(instance=product)
        return render(request, 'Produits/edit_product.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('Catalogue')
    return render(request, 'Produits/delete_product.html', {'product': product})


def detail_product(request, product_id):
    produit = get_object_or_404(Produit, id=product_id)
    context = {'produit': produit}
    return render(request, 'Produits/detail_product.html', context)


def Catalogue(request):
    products = Produit.objects.all()
    context = {'products': products}
    return render(request, 'Produits/mesProduits.html', context)

def indexA(request):
    return render(request, 'magasin/accueil.html')

def contact(request):
    return render(request,"contact/contact.html")

def about(request):
    return render(request,"about/about.html")
def cart(request):
    return render(request,"cart/cart.html")

def ListMembre(request):
    Membres = Membre.objects.all()
    context = {'Membres': Membres}
    return render(request, 'Membres/mesMembres.html', context)


def nouveauMembre(request):
    if request.method == "POST":
        form = MembreForm(request.POST, request.FILES)
        if form.is_valid():
            # Récupérer l'instance du modèle produit
            frns = form.save(commit=False)
            # Récupérer la nouvelle image téléchargée
            nouvelle_image = form.cleaned_data['logo']
            # Si une nouvelle image a été téléchargée, la sauvegarder
            if nouvelle_image:
                frns.logo = nouvelle_image
            # Sauvegarder le produit
            form.save()
            Membres = Membre.objects.all()
            return render(request, 'Membres/mesMembres.html', {'Membres': Membres})
    else:
        form = MembreForm()  # créer formulaire vide
        Membres = Membre.objects.all()
        return render(request, 'Membres/create_For.html', {'form': form, 'Membres': Membres})
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


class ChangePasswordView(PasswordChangeView):
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('home')


def edit_Membre(request, fk):
    membre = get_object_or_404(Membre, id=fk)
    if request.method == 'POST':
        form = MembreForm(request.POST, request.FILES, instance=membre)
        if form.is_valid():
            # Récupérer l'instance du modèle membre
            membre = form.save(commit=False)
            # Récupérer la nouvelle image téléchargée
            nouvelle_image = form.cleaned_data['logo']
            # Si une nouvelle image a été téléchargée, la sauvegarder
            if nouvelle_image:
                membre.logo = nouvelle_image
            # Sauvegarder le membre
            membre.save()
            return redirect('Membres')
    else:
        form = MembreForm(instance=membre)
        return render(request, 'Membres/edit_For.html', {'form': form})

def delete_Membre(request, fk):
    membre = get_object_or_404(Membre, id=fk)
    if request.method == 'POST':
        membre.delete()
        return redirect('Membres')
    return render(request, 'Membres/delete_For.html', {'Membre': membre})


def detail_Membre(request, for_id):
    membre = get_object_or_404(Membre, id=for_id)
    context = {'Membre': membre}
    return render(request, 'Membres/detail_For.html', context)


def add_to_panier(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    panier = Panier(user=request.user, project=project)
    panier.save()
    return redirect('panier:cart')  # Replace 'panier:cart' with your cart URL name


def create_Project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            # Access the saved project instance and assign the uploaded logo image
            project.logo = form.cleaned_data.get('logo')
            project.save()
            Projects = Project.objects.all()
            return render(request, 'Projects/mesProjects.html', {'Projects': Projects})
    else:
        form = ProjectForm()
        Projects = Project.objects.all()
        return render(request, 'Projects/create_Project.html', {'form': form, 'Projects': Projects})

def edit_Project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('ListProject')
    else:
        form = ProjectForm(instance=project)
        return render(request, 'Projects/edit_Project.html', {'form': form})


def delete_Project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('ListProject')
    return render(request, 'Projects/delete_Project.html', {'Project': project})


def detail_Project(request, Project_id):
    project = get_object_or_404(Project, id=Project_id)
    context = {'Project': project}
    return render(request, 'Projects/detail_Project.html', context)

#-----------------------------------------------CONTACT--------------------------------------------------------------------------
def contact(request):
    if request.method == 'POST':
        email = request.POST['email']
        subject=request.POST['subject']
        message = request.POST['message']

        message_body = f"Email: {email}\nSubject: {subject}\nMessage: {message}"

        send_mail(
            'Contact Form Submission',
            message_body,
            settings.DEFAULT_FROM_EMAIL,
            ['mohamedbenmannaa0@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'contact/contact.html', {'success': True})
    return render(request, 'contact/contact.html')



def ListProject(request):
    Projects = Project.objects.all()
    context = {'Projects': Projects}
    return render(request, 'Projects/mesProjects.html', context)


def create_categorie(request):
       if request.method == "POST" :
         form = CategorieForm(request.POST)
         if form.is_valid():
              form.save() 
              categories=Categorie.objects.all()
              
              return render(request,'Categories/mesCategories.html',{'categories':categories})
       else : 
            form = CategorieForm() #créer formulaire vide 
            categories=Categorie.objects.all()
            return render(request,'Categories/create_categorie.html',{'form':form,'categories':categories})

def edit_categorie(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)
    if request.method == 'POST':
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            categorie.save()
            return redirect('ListCategorie')
    else:
        form = CategorieForm(instance=categorie)
        return render(request, 'Categories/edit_categorie.html', {'form': form})

def delete_categorie(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)
    if request.method == 'POST':
        categorie.delete()
        return redirect('ListCategorie')
    return render(request, 'Categories/delete_categorie.html', {'categorie': categorie})


def detail_categorie(request, categorie_id):
    categorie = get_object_or_404(Categorie, id=categorie_id)
    context = {'categorie': categorie}
    return render(request, 'Categories/detail_categorie.html', context)

def ListCategorie(request):
    categories = Categorie.objects.all()
    context = {'categories': categories}
    return render(request, 'Categories/mesCategories.html', context)
