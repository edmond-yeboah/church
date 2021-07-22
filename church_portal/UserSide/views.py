from django.contrib import messages
from accounts.models import Customusers
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def userdash(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def sermons(request):
    return render(request,'sermons.html')


@login_required(login_url='login')
def profile(request):
    #get the user's username
    user = Customusers.objects.get(username=request.user.username)

    if request.method == "POST": #checking if a post request was sent
        try:
            fname = request.POST['fname'] #getting the first name entered by the user
            lname = request.POST['lname'] #getting the last name entered by the user
            tel = request.POST['phone'] #getting the phone number entered by the user
            bio = request.POST['bio'] #getting the bio entered by the user
            age = request.POST['age'] #getting the age entered by the user
            email = request.POST['email'] #getting the email entered by the user
            password = request.POST['password'] #getting the password entered by the user

            #checking if the user made a change of auth credentials change
            if len(password)>0: #if user submitted password

                #updating user's profile info
                user.first_name = fname
                user.last_name = lname
                user.tel = tel
                user.bio = bio
                user.age = age

                #for authentication side
                user.username = email
                user.email = email
                user.set_password(password)
                user.save()
                messages.info(request,"Profile update successful, Remember to login next time with your new credentials!")
                return redirect("/UserSide/profile/")
            
            else: #if user doesn't make change of auth credential request
                user.first_name = fname
                user.last_name = lname
                user.tel = tel
                user.bio = bio
                user.age = age
                user.save()
                messages.info(request,"Profile update successful")
                return redirect("/UserSide/profile/")
                
        except Exception as e: #if an error occur while getting the information
            print(e) #print error message to terminal

    return render(request,'profile.html')

@login_required(login_url='login')
def tithe(request):
    return render(request,'tithe.html')