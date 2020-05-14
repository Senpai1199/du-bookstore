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
    return render(request,'registrations/base.html', context = {"full_name": request.user.first_name + ' ' + request.user.last_name})

@login_required(login_url='login')
def home(request):
    """
        The HOME page of the portal where all the book listings would be displayed according to the year of the logged in user
    """
    books1 = Book.objects.filter(year=request.user.profile.year, sold=False)
    books2 = Book.objects.all().exclude(year=request.user.profile.year, sold=False)
    books = list(chain(books1, books2))
    print("****" + str(len(books)) + "*****")
    context = {
        "full_name": request.user.first_name + ' ' + request.user.last_name,
        "books": books
    }
    return render(request, 'registrations/home.html', context)

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


def sell_book(request):
    """
        Handles the form for adding an individual listing of book/reading to sell
    """
    if request.method == 'GET':
        books = Book.objects.filter(seller__auth_user=request.user)
        return render(request, 'registrations/sell_book.html', {'books': books})

    elif request.method == 'POST':
        data = request.POST.dict()
        email = data['email']
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            messages.warning(request, 'Please enter a valid email address.')
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            try:
                Participant.objects.get(user__email=data['email'])
                messages.warning(request, 'Email already registered.')
                return redirect(request.META.get('HTTP_REFERER'))
            except:
                pass
            participant = Participant()
            if not data['name']:
                messages.warning(request, 'Please enter guest name')
                return redirect(request.META.get('HTTP_REFERER'))
            if len(data['phone']) != 10:
                messages.warning(request, 'Please enter a valid phone number')
                return redirect(request.META.get('HTTP_REFERER'))
            try:
                phone = int(data['phone'])
            except:
                messages.warning(request, 'Please enter a valid phone number')
                return redirect(request.META.get('HTTP_REFERER'))
            # Create User Profile for guest or  not?
            name = ' '.join(str(data['name']).strip().split())
            gender = str(data['gender'])
            email = str(data['email'])
            user_profile = UserProfile(
                name=name, gender=gender, email=email, phone=phone)
            participant.city = str(data['city'])
            try:
                college = College.objects.get(name=str(data['college']))
            except:
                messages.warning(
                    request, 'Please select a college from the list.')
                return redirect(request.META.get('HTTP_REFERER'))
            participant.college = College.objects.get(
                name=str(data['college']))

            if not re.match(
                r'^20\d{2}(A[1-578B]([PT]S|A[1-578B]|B[1-5])|[CD]2[TP]S|B[1-5]([PT]S|A[1-578B])|H[DS0-9]\d{2}|PH[X0-9][PF0-9])\d{4}P$',
                    str(data['bits_id'])):
                messages.warning(request, 'Please enter a proper bits id')
                return redirect(request.META.get('HTTP_REFERER'))
            participant.referral = str(data['bits_id'])

            participant.is_guest = True
            participant.email_verified = True
            user_profile.save()
            participant.user = user_profile
            participant.save()
            participant.status = 5

            username = participant.user.name.split(
                ' ')[0] + str(participant.id)
            # random alphanumeric password of length 8
            password = ''.join(choice(chars) for i in range(8))
            user_1 = User(username=username, password=password)
            user_1.save()
            participant.user.auth_user = user_1
            participant.user.save()
            participant.save()  # Barcode will automatically be generated and assigned. Django Signals
            # sendgrid email body is written in a separate file called send_grid.py

            context = {
                'error_heading': "Emails sent",
                'message': "Login credentials have been mailed to the corresponding new participants.",
                'url': request.build_absolute_uri(reverse('regsoft:firewallz_home'))
            }
            return render(request, 'registrations/message.html', context)

    return render(request, 'registrations/sell_book.html', context)

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

