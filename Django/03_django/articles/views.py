from django.shortcuts import render, redirect

import articles
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article()
    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', article.pk)
    # return render(request, 'articles/create.html')

def detail(request, pk):
    print("detail")
    article = Article.objects.get(pk = pk)
    context = {'article':article,}

    return render(request, 'articles/detail.html',context)

def delete(request, pk):
    article=Article.objects.get(pk=pk)
    article.delete()

    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article':article}
    return render(request, 'articles/edit.html',context)

def update(request, pk):
    # pk로 수정할 게시글을 가져온다
    article = Article.objects.get(pk=pk)
    # request에서 사용자가 입력한 title과 content를 가져온다.
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    # DB에서 수정할 데이터로 조작한다
    article.save()
    # 모든 조작이 끝나면 어디론가 보낸다.
    return redirect("articles:detail",article.pk)