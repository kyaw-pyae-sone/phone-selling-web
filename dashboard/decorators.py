# dashboard/decorators.py
from django.shortcuts import redirect
from django.urls import reverse

def regular_user_required(view_func):
    """
    Decorator to restrict access for staff users.
    Redirects staff users to the dashboard.
    """
    def wrapper(request, *args, **kwargs):
        # Check if the user is a staff member
        if request.user.is_staff:
            # If so, redirect them to the dashboard's main page
            return redirect(reverse('dashboard:get_phone'))
        # If not, allow them to access the original view
        return view_func(request, *args, **kwargs)
    return wrapper