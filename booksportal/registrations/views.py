from django.shortcuts import render, redirect


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
    context = {
        "full_name": request.user.first_name + ' ' + request.user.last_name
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

