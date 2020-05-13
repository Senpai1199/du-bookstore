from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from itertools import chain

from registrations.models import Book

@login_required(login_url='login')
def index(request):
    """
        Redirect '/' to 'home/'
    """
    return redirect('home')

@login_required(login_url='login')
def base_view(request):
    return render(request,'registrations/base.html', context={"full_name": request.user.first_name + ' ' + request.user.last_name})

@login_required(login_url='login')
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

@csrf_exempt
def login_view(request):
    """
        Handles user's login 
    """

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('home'))
        else:
            return render(request, 'registrations/login.html')

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                try:
                    login(request, user)
                    return redirect('home')

                except Exception as e:
                    message = "User does not Exist."
                    context = {'error_heading':'No User','message' : message,'url':request.build_absolute_uri(reverse('login'))}
                    return render(request, 'registrations/message.html', context)

            # else:
            #     message="Your account is currently INACTIVE. To activate it, call the following members of the \
            #     Department of Publications and Correspondence. Daman: %s - pcr@bits-bosm.org .'%(utils.get_pcr_number()), \
            #     'url':request.build_absolute_uri(reverse('registrations:login'))"
            #     context = {'error_heading':'Email not verified','message':message}
            #     return render(request,'registrations/message.html',context)
        else:
            messages.warning(request, 'Invalid username/password. Please try again.')
            try:
                return redirect(request.META.get('HTTP_REFERER'))
            except:
                return redirect('login')

@login_required(login_url='login')
def logout_view(request):
    """
        Logout user from portal
    """
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def about(request):
    """
        The 'About Us' page
    """
    return render(request, 'registrations/about.html')

@login_required(login_url='login')
def contact(request):
    """
        The 'Contact Us' page
    """
    return render(request, 'registrations/contact.html')

