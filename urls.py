from django.urls import path
from . import views
urlpatterns = [
     path('project/', views.project,name='blog-project'),
    path('home/', views.home,name='blog-home'),
    path('contact/', views.contact,name='blog-contact'),
    path('index/', views.index,name='blog-index'),
    path('SHRUTHI K/roxy/', views.blog,name='blog-blog'),
    path('image-to-pattern/', views.imagetopattern,name='blog-Image-to-pattern'),
    
]




E:\SHRUTHI K\roxy\blog.html

