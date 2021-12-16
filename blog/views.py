from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Bloging


def all_blogs(request):
    all_zapisi = Bloging.objects.all()
    context = {'blogs': all_zapisi}
    return render(request, 'blog/all_blogs.html', context=context)


def detail(request, blog_id):
    blog = get_object_or_404(Bloging, pk=blog_id)
    context = {'id': blog}
    return render(request, 'blog/detail.html', context=context)
