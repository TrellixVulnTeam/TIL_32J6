from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)


def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    # print(f'에러: {form.errors}')
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)


    # 사용자의 데이터를 받아서
    # title = request.POST.get('title')
    # content = request.POST.get('content')

    # DB에 저장
    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2
    # article = Article(title=title, content=content)
    # article.save()

    # 3
    # Article.objects.create(title=title, content=content)

    # return render(request, 'articles/index.html')
    # return redirect('/articles/')
    # return redirect('articles:index')
    # return redirect('articles:detail', article.pk)


def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(request.POST, instance=article)
    # form = ArticleForm(data=request.POST, instance=article)
    if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
    # return redirect('articles:detail', article.pk)