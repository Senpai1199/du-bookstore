from django.shortcuts import render, redirect
from itertools import chain

from registrations.models import Book


def index(request):
    """
        Redirect '/' to 'home/'
    """
    return redirect('home')

def base_view(request):
    return render(request,'registrations/base.html', context={"full_name": request.user.first_name + ' ' + request.user.last_name})

def home(request):
    """
        The HOME page of the portal where all the book listings would be displayed according to the year of the logged in user
    """
    books1 = Book.objects.filter(year=request.user.profile.year)
    books2 = Book.objects.all().exclude(year=request.user.profile.year)
    books = list(chain(books1, books2))
    print("****" + str(len(books)) + "*****")
    context = {
        "full_name": request.user.first_name + ' ' + request.user.last_name,
        "books": books
    }
    return render(request, 'registrations/home.html')

def about(request):
    """
        The 'About Us' page
    """
    return render(request, 'registrations/about.html')

def contact(request):
    """
        The 'Contact Us' page
    """
    return render(request, 'registrations/contact.html')

