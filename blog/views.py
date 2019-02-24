from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse

#dummy list of dictionaries, since no DB
posts = [
    {
        'author': 'User1',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'User2',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

# create function to reply requests
def home(request):
    #return HttpResponse('<h1> Blog Home </h1>')
    context = {
        'posts_var' : Post.objects.all()

    }
    return render(request, 'blog/home.html', context)


def about(request):
    #return HttpResponse('About function in views.py')
    title = {
        'title' : "sent from views"
    }
    return render(request, 'blog/about.html', title)