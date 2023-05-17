from django.urls import path
from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     path('products/', views.index, name='index'),
    path('', views.indexA, name='indexA'),
    path('Membres/', views.ListMembre, name='Membres'),
    path('about/',views.about,name="about" ),
    path('cart/',views.cart,name="cart" ),
    path('Catalogue/', views.Catalogue, name='Catalogue'),
    path('nouvMembre/',views.nouveauMembre,name='nouvMembre'),
    path('register/',views.register, name = 'register'), 
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('contact/',views.contact,name="contact" ),
    path('editMembre/<int:fk>/', views.edit_Membre, name='edit_Membre'),
    path('deleteMembre/<int:fk>/', views.delete_Membre, name='delete_Membre'),
    path('Membre/<int:for_id>/', views.detail_Membre, name='detail_Membre'),

    path('editProduct/<int:pk>/', views.edit_product, name='edit_product'),
    path('deleteProduct/<int:pk>/', views.delete_product, name='delete_product'),
    path('Product/<int:product_id>/', views.detail_product, name='detail_product'),

    path('ListProject/', views.ListProject, name='ListProject'),
    path('create_Project/',views.create_Project,name='create_Project'),
     path('editProject/<int:pk>/', views.edit_Project, name='edit_Project'),
    path('deleteProject/<int:pk>/', views.delete_Project, name='delete_Project'),
    path('Project/<int:Project_id>/', views.detail_Project, name='detail_Project'),

    path('ListCategorie/', views.ListCategorie, name='ListCategorie'),
    path('create_categorie/',views.create_categorie,name='create_categorie'),
    path('editCategorie/<int:pk>/', views.edit_categorie, name='edit_categorie'),
    path('deleteCategorie/<int:pk>/', views.delete_categorie, name='delete_categorie'),
    path('Categorie/<int:categorie_id>/', views.detail_categorie, name='detail_categorie'),
  

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
