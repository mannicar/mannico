from django.shortcuts import render

# Create your views here.

from blog.models import Article

def blog(request):
    articles_db = Article.objects.all()
    articles=[]
    for a in articles_db:
        articles.append({'title':a.title, 'body':a.body, 'author':a.author, 'pub_date':a.pub_date})
    context = {
        "articles": articles
    }

    return render(request, 'blog.html', context=context)