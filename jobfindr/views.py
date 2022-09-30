# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
# App
from jobfindr.models import JobSeeker, TalentHunter, Profile
# Third party
from django_nextjs.render import render_nextjs_page_sync
# Built in
import json

# NextJS templates
def nextjs_index(request):
    return render_nextjs_page_sync(request)

def nextjs_login(request):
    return render_nextjs_page_sync(request)

def nextjs_register(request):
    return render_nextjs_page_sync(request)

def nextjs_congratulations(request):
    return render_nextjs_page_sync(request)

def nextjs_profile(request):
    return render_nextjs_page_sync(request)

# API endpoints
def api_hello(request):
    # Test route
    if request.method == "GET":
        return JsonResponse({'msg': 'Hello world! as JSON'})

def api_register(request):
    """Register a new user"""
    if request.method == "POST":
        # https://stackoverflow.com/questions/29780060
        # /trying-to-parse-request-body-from-post-in-django
        body = json.loads(request.body)

        # Store form field values
        username = body.get("username")
        email = body.get("email")
        usertype = body.get("usertype")
        password = body.get("password")
        cpassword = body.get("cpassword")

        # Check if fields are empty
        for field in [username, email, usertype, password, cpassword]:
            if not field:
                return JsonResponse(
                    {
                        'msg': 'There must be no empty fields'
                    },
                    status=400
                )

        # Check if password confirmation matches
        if password != cpassword:
            return JsonResponse(
                {
                    'msg': 'Password and confirmation password doesn\'t match'
                },
                status=400
            )

        # Create new user accordingly to the usertype
        if usertype == 'jobseeker':
            try:
                user = JobSeeker.objects.create_user(username, email, password)
                user.save()
                profile = Profile.objects.create(owner=user)
                profile.save()
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
                profile = Profile.objects.create(owner=user)
                profile.save()
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
                },
                status=400
            )

def api_login(request):
    """Log in user"""
    if request.method == "POST":
        # https://stackoverflow.com/questions/29780060
        # /trying-to-parse-request-body-from-post-in-django
        body = json.loads(request.body)
        # Get form values
        username = body.get('username')
        password = body.get('password')  

        if username == '' or password == '':
            return JsonResponse({
                'msg': 'You must provide your username and password'
            }, status=400)

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
        return HttpResponseRedirect(reverse('login'))

@login_required(redirect_field_name="")
def api_logout(request):
    # Don't accept requests other than GET
    if request.method != "GET":
        return HttpResponseRedirect(reverse('login'))
    
    # Redirects user to login page if not authenticated
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    # Perform log out action
    logout(request)
    return JsonResponse({
        'msg': 'Logged out'
    })

def api_user(request):
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

def api_get_profile(request, username=None):
    """Get profile information"""
    if request.method == "GET":
        if not username and not request.user.is_authenticated:
            # Redirect to login page if not authenticated
            # TODO: Fix NoReverseMatch at /api/pros/
            return HttpResponseRedirect(reverse('login'))
        elif not username and request.user.is_authenticated:
            # Redirect to user profile if authenticated and not username is provided
            # TODO: Fix NoReverseMatch at /api/pros/
            return HttpResponseRedirect(reverse('api_profile_user'), kwargs={'username': str(request.user.username)})

        # TODO: Identify user type and process view accordingly

        # Query database
        user_query = JobSeeker.objects.filter(username=username) or TalentHunter.objects.filter(username=username)
        if len(user_query):
            # Return user profile JSON if found
            user = user_query[0]
            profile = Profile.objects.get(owner=user.id)
            return JsonResponse({'profile': profile.get_profile_as_dict()})
        else:
            # Return return user not found 
            return JsonResponse({'msg': 'User not found'}, status=404)