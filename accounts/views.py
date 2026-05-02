
# Create your views here.

from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from .models import User



def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user_type = request.POST['user_type']

        user = User.objects.create_user(
            username=username,
            password=password,
            user_type=user_type
        )

        return redirect('login')

    return render(request, 'accounts/register.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            print("USER TYPE:", user.user_type)  # DEBUG

            if user.user_type == 'admin':
                return redirect('admin_dashboard')
            else:
                return redirect('student_dashboard')

        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')