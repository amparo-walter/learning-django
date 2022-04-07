from django.shortcuts import render
from .models import *

# Create your views hered

def articles_view(request):
    
    context = {}
    articles = Article.objects.all()
    context['articles'] = articles
    
    return render(request, 'articles/articles.html', context)

def articles_create_view(request):
    context = {}
    form = ArticleForm()
    
    if not request.POST:
        context['form'] = form
        context['created'] = False
    else:
        context['created'] = True
        title = request.POST['title']
        content = request.POST['content']
        
        Article.objects.create(title=title, content=content)
        
        context['title'] = title
    
    
    return render(request, 'articles/create.html', context)  
