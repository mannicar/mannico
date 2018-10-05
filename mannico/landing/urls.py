from django.urls import path
from landing import views
from blog import views as blog_views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('blog', blog_views.blog, name='blog'),
    path('blog_placeholder', views.blog_placeholder, name='blog_placeholder'),
    path('mannicode', views.mannicode, name='mannicode'),
    path('contact', views.contact, name='contact'),
]
