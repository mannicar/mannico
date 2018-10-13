from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'context_test_variable' : 'None, yet!'
    }
    return render(request, "index.html", context=context)

def mannicode(request):
    return render(request, "mannicode.html", context={})

def contact(request):
    return render(request, "contact.html", context={})