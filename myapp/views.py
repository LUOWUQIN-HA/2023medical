from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """首页视图，显示20231201031 liuwei"""
    content = "20231201031 liuwei"
    return render(request, 'myapp/index.html', {'content': content})