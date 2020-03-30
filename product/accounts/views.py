from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    #need to route to home page
    return render(request, 'signup.html')
