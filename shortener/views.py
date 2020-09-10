import socket
from random import choice
from string import ascii_letters, digits

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import ShortUrl



def short_url(request, url):

    ret = get_object_or_404(ShortUrl, short_url=url)

    return redirect(ret.long_url)


@login_required(login_url='/accounts/login/')
def add(request):

    if request.method == "POST":
        new_link = ShortUrl.objects.create(short_url=get_random_url(), long_url=request.POST['url'])
        return redirect('/link/' + str(new_link.id))
    else:
        return render(request, 'shortener/add.html') 


class LinkDetailView(DetailView):
    model = ShortUrl

@login_required(login_url='/accounts/login/')
def links_list(request):
    a = request.user.shorturl_set.all()
    print(a)
    return render(request, 'shortener/links_list.html', {'object_list': a})


def get_random_url():
    random_string = ''.join(choice(ascii_letters+digits) for i in range(5))

    while ShortUrl.objects.filter(short_url=random_string).exists():

        get_random_url()

    return random_string
