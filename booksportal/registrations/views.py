from django.shortcuts import render

# Create your views here.
def base_view(request):
    return render(request,'registrations/base.html', context={})

def about(request):
    return render(request, 'registrations/about.html')

def contact(request):
    return render(request, 'registrations/contact.html')

