from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserDetails 


def homepage(request):
    return render(request, 'homepage.html')  
def get_all_users(request):
    users = list(UserDetails.objects.values())  
    return JsonResponse(users, safe=False)

def get_user_by_email(request, email):
    user = UserDetails.objects.filter(email=email).values().first()  
    if user:
        return JsonResponse(user, safe=False)
    return JsonResponse({'error': 'User not found'}, status=404)  

def delete_user(request, email):
    deleted_count, _ = UserDetails.objects.filter(email=email).delete() 
    if deleted_count:
        return JsonResponse({'message': 'User deleted successfully'})
    return JsonResponse({'error': 'User not found'}, status=404)  

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if UserDetails.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('signup')

        UserDetails.objects.create(username=username, email=email, password=password)
        messages.success(request, "Signup successful! Please login.")
        return redirect('login')

    return render(request, 'signup.html')
def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = UserDetails.objects.filter(email=email, password=password).first()
        if user:
            messages.success(request, "Login successful! Welcome, " + user.username)
            return redirect('success')  
        else:
            messages.error(request, "Invalid email or password!")
            return redirect('login')

    return render(request, 'login.html')

def success(request):
    return render(request, 'success.html')

