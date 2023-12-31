from django.shortcuts import render

# Create your views here.
def register_user(request):
    return render(request, template_name='accounts/register-page.html')


def login_user(request):
    return render(request, template_name='accounts/login-page.html')


def profile_details(request, pk=1):
    return render(request, template_name='accounts/profile-details-page.html')


def profile_edit(request, pk):
    return render(request, template_name='accounts/profile-edit-page.html')


def profile_delete(request, pk):
    return render(request, template_name='accounts/profile-delete-page.html')