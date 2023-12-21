from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.utils import timezone
from datetime import datetime
from .models import News
from .rss_parser import parse_rss

def home(request):
    # lenta_news_url = 'https://lenta.ru/rss'
    # lenta_news = parse_rss(lenta_news_url)
    #
    # for entry in lenta_news:
    #     # Convert the date string to a datetime object
    #     published_date = datetime.strptime(entry['published'], '%a, %d %b %Y %H:%M:%S %z')
    #
    #     # Check if the datetime is naive (not timezone-aware)
    #     if timezone.is_naive(published_date):
    #         # Convert the datetime to the timezone-aware object
    #         published_date = timezone.make_aware(published_date)
    #
    #     News.objects.create(
    #         title=entry['title'],
    #         link=entry['link'],
    #         summary=entry['summary'],
    #         published=published_date,
    #         category=entry['category']
    #     )

    all_news = News.objects.all().order_by('-published')

    paginator = Paginator(all_news, 20)
    page = request.GET.get('page', 1)

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    return render(request, 'newsapp/home.html', {'news': news})



def news_by_category(request, category):
    categories_dict = {'travel': 'Путешествия',
                       'world': 'Мир',
                       'economics': 'Экономика',
                       'russia': 'Россия',
                       'tech': 'Наука и техника',
                       'sport': 'Спорт',
                       'internet': 'Интернет и СМИ'}
    category = categories_dict.get(category)
    all_news = News.objects.filter(category=category).order_by('-published')

    paginator = Paginator(all_news, 20)
    page = request.GET.get('page', 1)

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    return render(request, 'newsapp/category.html', {'news': news, 'category': category})