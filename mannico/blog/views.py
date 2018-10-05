from django.shortcuts import render

# Create your views here.

from blog.models import Article

def blog(request):
    articles = Article.objects.all()
    context = {
        "articles": articles
    }

    return render(request, 'blog.html', context=context)