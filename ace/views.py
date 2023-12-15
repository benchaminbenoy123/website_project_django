from django.conf import settings
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from . models import Profile
from django.contrib.auth.models import User
from django.shortcuts import render, redirect




# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('USERNAME')
        password = request.POST.get('PASSWORD')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

# def registration(request):
#     if request.method == "POST":
#         username = request.POST.get("USERNAME")
#         firstname = request.POST.get("FIRSTNAME")
#         lastname = request.POST.get("LASTNAME")
#         email = request.POST.get("EMAIL")
#         password = request.POST.get("PASSWORD")
#         confirm_password = request.POST.get("CONFIRM_PASSWORD")
#         gender = request.POST.get("GENDER")
#         phone_number = request.POST.get("PHONE_NUMBER")
#         country = request.POST.get("COUNTRY")
#         city = request.POST.get("CITY")
#         dob = request.POST.get("DATE OF BIRTH")
#         uploaded_file = request.FILES.get("file")
#
#         if password == confirm_password:
#             if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
#                 return redirect("registration")
#             else:
#                 # Create user using create_user method for password hashing
#                 user = User.objects.create_user(
#                     username=username,
#                     email=email,
#                     password=password,
#                     first_name=firstname,
#                     last_name=lastname,
#                 )
#
#                 # Create and save Profile details for the user
#                 profile = Profile(
#                     user=user,
#                     gender=gender,
#                     phone_number=phone_number,
#                     country=country,
#                     city=city,
#                     dob=dob,
#                     image=uploaded_file,
#                 )
#                 profile.save()
#                 return redirect("login")
#         else:
#             return render(request, 'registration.html')
#     else:
#         return render(request, 'registration.html')
#
#
# def registration(request):
#     if request.method == 'POST':
#         username = request.POST.get('USERNAME')
#         firstname = request.POST.get('FIRSTNAME')
#         lastname = request.POST.get('LASTNAME')
#         email = request.POST.get('EMAIL')
#         password = request.POST.get('PASSWORD')
#         confirm_password = request.POST.get('CONFIRM_PASSWORD')
#
#         # Check if passwords match
#         if password == confirm_password:
#             # Check if username or email already exists
#             if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
#                 return redirect("registration")
#             else:
#                 # Create a new user
#                 user = User.objects.create_user(
#                     username=username,
#                     first_name=firstname,
#                     last_name=lastname,
#                     email=email,
#                     password=password
#                 )
#
#                 # Create and save user profile details
#                 details = Profile()
#                 details.user = user
#                 details.gender = request.POST.get('GENDER')
#                 details.phone_number = request.POST.get('PHONE_NUMBER')
#                 details.city = request.POST.get('CITY')
#                 details.dob = request.POST.get('DOB')
#                 details.country = request.POST.get('COUNTRY')
#
#                 # Handle image upload
#                 if 'file' in request.FILES:
#                     details.image = request.FILES['file']
#
#                 details.save()
#                 # Redirect to a success page or login page
#                 return redirect('login')  # Change 'success' to your desired success page
#         else:
#             # Passwords don't match, redirect back to registration page
#             return redirect('registration')
#     else:
#         # Render the registration form
#         return render(request, 'registration.html')

def registration(request):
    if request.method == 'POST':

        username = request.POST.get('USERNAME')
        firstname= request.POST.get('FIRSTNAME')
        lastname = request.POST.get('LASTNAME')
        email = request.POST.get('email')
        password = request.POST.get('PASSWORD')
        confirm_password = request.POST.get('CONFIRM_PASSWORD')

        # Check if passwords match
        if password == confirm_password:
            # Check if username or email already exists
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                return redirect('registration')
            else:
                # Create a new user
                user = User.objects.create_user(
                    username=username,
                    first_name=firstname,
                    last_name=lastname,
                    email=email,
                    password=password
                )
                subject="welcome to vintage info solutions"
                message=f"{user.username},thankyou for registering in vintage info solutions"
                email_form=settings.EMAIL_HOST_USER
                recipient_list=[user.email]
                send_mail(subject,message,email_form,recipient_list)

                # Create and save user profile details
                details = Profile()
                details.user = user
                details.gender = request.POST.get('gender')
                details.phone_number = request.POST.get('phone')
                details.city = request.POST.get('city')
                details.dob = request.POST.get('DATE OF BIRTH')
                details.country = request.POST.get('country')

                # Handle image upload
                if 'file' in request.FILES:
                    details.image = request.FILES['file']

                details.save()
                # Redirect to a success page or login page
                return redirect('login')  # Change 'login' to your desired success page
        else:
            # Passwords don't match, redirect back to registration page
            return redirect('registration')
    else:
        # Render the registration form
        return render(request, 'registration.html')

def about(request):
    return render(request,'about.html')
def courses(request):
    return render(request,'courses.html')
@login_required
def dashboard(request):
    user = request.user
    try:
       Profile_data=Profile.objects.get(user=user)
    except Profile.DoesNotExist:
       Profile_data=None
    print("profile not exist",user)
    context={"userDetails":user,"profiledata": Profile_data}


    return render(request, 'dashboard.html',context)
def logout(request):
    auth.logout(request)
    return redirect("home")