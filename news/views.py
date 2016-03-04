from django.shortcuts import render
from .models import Article


# Create your views here.
def year_archive(request, year):
    a_list = Article.object.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)
