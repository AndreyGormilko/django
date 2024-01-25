from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm, CustomAuthenticationForm
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth.models import User

# Create your views here.
class CustomLoginView(AuthLoginView):
    form_class = CustomAuthenticationForm
    template_name = 'registration/login.html'

def register(request):
    if request.method != 'POST':
        form = RegistrationForm()
    else:
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('main:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)

def profile(request, user_id):
    user = User.objects.get(id=user_id)
    context = {'user': user}
    return render(request, 'users/profile.html', context)
