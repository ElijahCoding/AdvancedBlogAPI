from django.shortcuts import render
from .models import Article, Feed
from .forms import FeedForm

# Create your views here.
def articles_list(request):
    articles = Article.objects.all()
    return render(request, 'articles_list.html', { 'articles': articles })

def feeds_list(request):
    feeds = Feed.objects.all()
    return render(request, 'feeds_list.html', { 'feeds': feeds })

def new_feed(request):
    form = FeedForm
    return render(request, 'new_feed.html', { 'form': form })
