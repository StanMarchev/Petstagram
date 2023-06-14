from django.shortcuts import render

# Create your views here.
def register_user(request):
    return render(request, template_name='accounts/register-page.html')


def login_user(request):
    return render(request, template_name='accounts/login-page.html')


def profile_details(request):
    return render(request, template_name='accounts/profile-details-page.html')


def profile_edit(request):
    return render(request, template_name='accounts/profile-edit-page.html')


def profile_delete(request):
    return render(request, template_name='accounts/profile-delete-page.html')