from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'context_test_variable' : 'None, yet!'
    }
    return render(request, "index.html", context=context)

def blog_placeholder(request):
    return render(request, "blog_placeholder.html", context={})