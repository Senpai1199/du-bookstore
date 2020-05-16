from django.contrib import messages
from django.shortcuts import redirect

from registrations.models import UserProfile

def has_profile_completed(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        try:
            profile = UserProfile.objects.get(auth_user=request.user)
            return function(request, *args, **kwargs)
        except UserProfile.DoesNotExist:
            messages.error(request, "Please complete your profile details first.")
            return redirect('complete_profile') 
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap