from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


