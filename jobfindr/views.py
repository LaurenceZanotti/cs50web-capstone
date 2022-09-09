from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render
from django.http import JsonResponse
from jobfindr.models import JobSeeker, TalentHunter

# Create your views here.
def index(request):
    if request.method == "GET":
        return render(request, "jobfindr/index.html")

def hello(request):
    if request.method == "GET":
        return JsonResponse({'msg': 'Hello world! as JSON'})

def register(request):
    """Register a new user"""
    if request.method == "POST":
        # Store form field values
        username = request.POST["username"]
        email = request.POST["email"]
        usertype = request.POST["usertype"]

        # Check if fields are empty
        for field in [username, email, usertype]:
            if not field:
                return JsonResponse(
                    {
                        'msg': 'There must be no empty fields'
                    }
                )

        # Check if password confirmation matches
        password = request.POST["password"]
        cpassword = request.POST["cpassword"]
        if password != cpassword:
            return JsonResponse(
                {
                    'msg': 'Password and confirmation password doesn\'t match'
                }
            )

        # Create new user accordingly to the usertype
        if usertype == 'jobseeker':
            try:
                user = JobSeeker.objects.create_user(username, email, password)
                user.save()
            except IntegrityError:
                return JsonResponse({
                    'msg': 'User already exists'
                }, status=409)
            return JsonResponse({
                'msg': "User created!"
            }, status=201)
            
        elif usertype == 'talenthunter':
            try:
                user = TalentHunter.objects.create_user(username, email, password)
                user.save()
            except IntegrityError:
                return JsonResponse({
                    'msg': 'User already exists'
                }, status=409)
            return JsonResponse({
                'msg': "User created!"
            }, status=201)
        else:
            return JsonResponse(
                {
                    'msg': 'User must tell if they are looking for jobs or talents'
                }
            )

def login_view(request):
    """Log in user"""
    if request.method == "POST":
        # Get form values
        username = request.POST['username']
        password = request.POST['password']

        # Attempt to authenticate and log user in
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({
                'msg': 'Logged in successfully!'
            })
        else:
            return JsonResponse({
                'msg': 'Invalid username and/or password.'
            }, status=401)
    else:
        return JsonResponse({
            'msg': 'Forbidden'
        }, status=403)

def logout_view(request):
    logout(request)
    return JsonResponse({
        'msg': 'Logged out'
    })

def user(request):
    """Returns user information if user is authenticated"""
    if request.method == "GET" and request.user.is_authenticated:
        return JsonResponse({
            'user': {
                'id': request.user.pk,
                'username': request.user.username
            }
        })
    else:
        return JsonResponse({
            'user': None,
            'error': 'Not authenticated'
        }, status=403)
