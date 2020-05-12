from django.shortcuts import render

# Create your views here.
def base_view(request):
    return render(request,'registrations/base.html', context={})
