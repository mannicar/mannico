from django.urls import path
from landing import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('blog_placeholder', views.blog_placeholder, name='blog_placeholder'),
    path('mannicode', views.mannicode, name='mannicode'),
    path('contact', views.contact, name='contact'),
]
