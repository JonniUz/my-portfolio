from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Portfolio
from .forms import MessageForm


def index(request):
    form = MessageForm()
    portfolios = Portfolio.objects.all()
    context = {
        'portfolios': portfolios,
        'form': form
    }
    return render(request, 'index.html', context)


def receive_message(request):
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Profile details updated for {user}')
            return HttpResponseRedirect(reverse('thanks'))
    context = {
        'form': form
    }
    return render(request, 'index.html', context)


def contact_thank(request):
    return render(request, 'thanks.html')
