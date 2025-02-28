from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('', views.landingpage, name='landingpage'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('herimorrhagic', views.herimorrhagic, name='herimorr'),
    path('ishemic_cancer', views.ishemic_cancer, name='ishemic_cancer'),
    path('tia/', views.tia, name='tia'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutusers, name='logout'),
    path('predict/', views.generation_model, name='generation_model'),
    path('speed/', views.speed_model, name='speed_model'),


]
