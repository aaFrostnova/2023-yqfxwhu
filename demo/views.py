from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request, num):
    return HttpResponse(f"Hello world{num}!")

def index(request):
    context = {
        "news_list" : [
            {
                "title":"第一篇新闻",
                "content":"哈哈哈哈成功了",
            },
            {
                "title":"第二篇新闻",
                "content":"哈哈哈哈又成功了",
            },
        ]
    }
    return render(request, "./index.html", context=context)

def graph(request):
    return render(request, "./graph-label-overlap.html")

def graphofone(request):
    return render(request, "./graph-of-one.html")