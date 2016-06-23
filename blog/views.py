from django.shortcuts import render_to_response
from blog.models import BlogPost


def homepage(request):
    data = {
        'title': 'Titleee',
        'data1': 'Horayyy',
        'blog_list': BlogPost.objects.all(),
    }
    return render_to_response('index.html', data)
