from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View
from django.urls import reverse_lazy

def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'You are logged in as {username}')
                return redirect(reverse_lazy('home'))
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        login_form = AuthenticationForm()
        
    return render(request, 'login.html', {'login_form': login_form})


class RegisterView(View):
    def get(self, request):
        register_form = UserCreationForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = UserCreationForm(data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            password = register_form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=password)
            login(request, user)
            messages.success(request, f'Account created successfully for {user.username}')
            return redirect(reverse_lazy('home'))
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
            return render(request, 'register.html', {'register_form': register_form})
