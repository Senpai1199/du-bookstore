from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from itertools import chain

from registrations.models import Book, Course, UserProfile

@login_required(login_url='login')
def index(request):
    """
        Redirect '/' to 'home/'
    """
    return redirect('home')

@login_required(login_url='login')
def base_view(request):
    return render(request,'registrations/base.html', context={})

@login_required(login_url='login')
def home(request):
    """
        The HOME page of the portal where all the book listings would be displayed according to the year of the logged in user
    """
    books1 = Book.objects.filter(year=request.user.profile.year, sold=False)
    books2 = Book.objects.all().exclude(year=request.user.profile.year, sold=False)
    books = list(chain(books1, books2))
    context = {
        "books": books
    }
    return render(request, 'registrations/home.html', context=context)

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

@csrf_exempt
@login_required(login_url='login')
def sell_book(request):
    """
        Handles the form for adding an individual listing of book/reading to sell
    """
    if request.method == 'GET':
        books = Book.objects.filter(seller__auth_user=request.user)
        return render(request, 'registrations/sell_book.html', {"courses": Course.objects.all()})

    elif request.method == 'POST':
        data = request.POST
        try: # for required values
            title = str(data['title'])
            condition = str(data['condition'])
            course_name = str(data['course_name'])
            year = data['year']
            semester = int(data['semester'])
            price = int(data['price'])
            book_type = str(data["type"]) # contains exact category value 'B' or 'R'
        except KeyError as e:
            messages.error(request, "Missing Field {}".format(e))
            return render(request, 'registrations/sell_book.html', {"courses": Course.objects.all()})
        except ValueError as value_error:
            messages.error(request, "Invalid Value: {}".format(value_error))
            return render(request, 'registrations/sell_book.html', {"courses": Course.objects.all()})

        try:
            seller = UserProfile.objects.get(auth_user=request.user)
        except UserProfile.DoesNotExist:
            messages.error(request, "Please complete your profile details first.")
            return render(request, 'registrations/sell_book.html', {"courses": Course.objects.all()})

        if book_type == "B":
            try:
                edition = data["edition"] # optional for Reading
                edition = edition.strip()
            except KeyError as e:
                messages.warning(request, "You must enter an edition if you're adding a book.")
                return redirect(request.META.get('HTTP_REFERER'))
        try:
            book_image = request.FILES["file"]
        except Exception as e:
            print(e)
            messages.warning(request, "Please upload an image for your listing.")
            return render(request, 'registrations/sell_book.html', {"courses": Course.objects.all()})
            # print(book_image)
            # if book_image is None:
        
        try:
            course = Course.objects.get(name=course_name)
        except Course.DoesNotExist:
            messages.warning(request, "Please select a course from the list.")
            return render(request, 'registrations/sell_book.html', {"courses": Course.objects.all()})
        
        if year == "Masters":
            year = 4
            semester = 7
        if semester == 1:
            offset = 0
        else:
            offset = 1

        semester = int(year)*2 + int(offset)
        title = title.strip()
        condition = condition.strip()
        try:
            contains_notes = data["notes"]
            contains_notes = True
        except KeyError:
            contains_notes = False
        
        if book_type == "B":
            new_book = Book.objects.create(
                                        title=title, 
                                        category=book_type, 
                                        contains_notes=contains_notes, 
                                        condition=condition, 
                                        year=year, 
                                        semester=semester,
                                        image=book_image,
                                        course=course,
                                        price=price,
                                        seller=seller
                                    )
        else:
            new_book = Book.objects.create(
                                    title=title, 
                                    category="R", 
                                    contains_notes=contains_notes, 
                                    condition=condition, 
                                    year=year, 
                                    semester=semester,
                                    image=book_image,
                                    course=course,
                                    price=price,
                                    seller=seller
                                )
        try:
            description = str(data["description"])
            description = description.strip()
            new_book.description = description
            new_book.save()

            context = {
                'error_heading': "Success!",
                'message': "Listing has been added and will be available for the sellers to see.",
                'url': request.build_absolute_uri(reverse('sell_book'))
            }
            return render(request, 'registrations/message.html')
        except KeyError:
            context = {
                'error_heading': "Success!",
                'message': "Listing has been added and will be available for the sellers to see.",
                'url': request.build_absolute_uri(reverse('sell_book'))
            }
            return render(request, 'registrations/message.html')

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

@login_required(login_url='login')
def search(request):
    """
        The HOME page of the portal where all the book listings would be displayed according to the year of the logged in user
    """

    if request.method == 'GET':
        context = {}
    else:
        books1 = Book.objects.filter(year=request.user.profile.year, sold=False)
        books2 = Book.objects.all().exclude(year=request.user.profile.year, sold=False)
        books = list(chain(books1, books2))
        print("****" + str(len(books)) + "*****")
        context = {
            "books": books
        }
    return render(request, 'registrations/search.html', context=context)
