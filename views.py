from django.shortcuts import render

from blog.models import Post


def index_peg(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})