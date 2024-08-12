

from django.shortcuts import render
from django.views.generic import ListView
from .models import News
from news_app.models import News

def news_list_view(request):
    news_list = News.published.all()
    news = News.published.all()[:5]
    xorij_news = News.published.filter(category__name = 'Xorij')[:4]
    mahalliy_news = News.published.filter(category__name = 'Mahalliy')[:4]
    sport_news = News.published.filter(category__name = 'Sport')[:5]
    texnology_news = News.published.filter(category__name = 'Texnologiya')[:5]
    huquq_news = News.published.filter(category__name = 'Huquq')
    photo_news = News.published.filter(category__name = 'Photo')


    context = {
        'news_list': news_list,
        'xorij_news': xorij_news,
        'mahalliy_news': mahalliy_news,
        'sport_news': sport_news,
        'texnology_news': texnology_news,
        'huquq_news': huquq_news,
        'photo_news': photo_news,
        'news':news,
    }
    return render(request, 'index.html', context)

class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'


def new_detail_view(request, slug):
    news = News.objects.get(slug=slug)
    three_news = News.published.filter(category__name = news.category.name).exclude(id=news.id)[:1]
    context = {
        'news': news,
        'three_news': three_news,
    }

    return render(request, 'single_page.html', context)

def contact_view(request):

    return render(request, template_name='contact.html')

def local_news_view(request):
    news_list = News.published.filter(category__name = 'Mahalliy')

    context = {'news_list': news_list}

    return render(request, 'local_news.html', context)

def xorij_news_view(request):
    news_list = News.published.filter(category__name = 'Xorij',)

    xorij = {'news_list': news_list}

    return render(request, 'xorij_news.html', xorij)

def sport_news_view(request):
    news_list = News.published.filter(category__name = 'Sport',)

    sport = {'news_list': news_list}

    return render(request, 'sport_news.html', sport)

def texnalogiya_news_view(request):
    news_list = News.published.filter(category__name = 'Texnologiya',)

    texnalogiya = {'news_list': news_list}

    return render(request, 'texnalogiya_news.html', texnalogiya)

def madaniyat_news_view(request):
    news_list = News.published.filter(category__name = 'Madaniyat',)

    madaniyat = {'news_list': news_list}

    return render(request, 'texnalogiya_news.html', madaniyat)