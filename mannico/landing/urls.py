from django.urls import path
from landing import views


urlpatterns = [
    path('', views.index, name='index'),
    path('blog_placeholder', views.blog_placeholder, name='blog_placeholder')
]
