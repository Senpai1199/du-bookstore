from django.shortcuts import render

# Create your views here.
def base_view(request):
    return render(request,'registrations/base.html', context={"full_name": request.user.first_name + ' ' + request.user.last_name})

def about(request):
    return render(request, 'registrations/about.html')

def contact(request):
    return render(request, 'registrations/contact.html')

