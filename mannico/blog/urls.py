from django.urls import path
from blog import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog', views.blog, name='blog')
]
