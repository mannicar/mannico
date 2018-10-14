from django.urls import path
from blog import views as blog_views
from landing import views as landing_views


urlpatterns = [
    path('', blog_views.blog, name='blog'),
    path('blog', blog_views.blog, name='blog'),
    path('mannicode', landing_views.mannicode, name='mannicode'),
    path('contact', landing_views.contact, name='contact'),
]
