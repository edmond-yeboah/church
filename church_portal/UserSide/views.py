from django.contrib import messages
from accounts.models import Customusers
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from AdminSide.models import sermon
from .models import comment
from django.db.models import Q

# Create your views here.
@login_required(login_url='login')
def userdash(request):
    return render(request, 'home.html')




@login_required(login_url='login')
def sermons(request):
    context={}
    if request.method=="POST": #checking if a post request was received
        action = request.POST['action'] #getting the type of button that was clicked

        if action=="search": #if user clicked the search button
            searchquery = request.POST['searchquery'] #get the search query entered by the user
            if len(searchquery)>0: #if user enteres search query
                searchresults = sermon.objects.filter(Q(title__icontains=searchquery)) #searching sermons by title
                if len(searchresults)>0: #if search matched any sermon in the database
                    context["allsermons"] = searchresults #display sermon to the user
                else: #if search didn't match any sermon in the database
                    context["nosermonresult"] = "No sermon title matches search query "+"'"+searchquery+"'" #display this message to admin
            else:
                context["nothingentered"] = "No search query entered" #display message if user doesnt enter search query
        elif action=="comment": #if user clicked to comment on a sermon
            comments = request.POST['comment'] #get the comment entered by the user
            sermonid = request.POST['sid'] #get the sermon id of sermon user commented on
            user = Customusers.objects.get(id = request.user.id)#get the user who commented
            
            SermonCommentedOn = sermon.objects.get(id=sermonid) #getting the sermon commented on with the id
            newcomment = comment()
            newcomment.by=user #setting the user who commented
            newcomment.cfor = SermonCommentedOn #setting the sermon this comment belongs to
            newcomment.content = comments #setting the comment content
            newcomment.save() #saving the comment
            context['sdetails'] = SermonCommentedOn #putting the sermon fetched into the context list

            #fetching comments for sermon
            SermonComments = comment.objects.filter(cfor=SermonCommentedOn) #fetching comments for the sermon
            context['comments'] = SermonComments #putting comments in a context list
             
    elif "sid" in request.GET: #if user click to view details of a sermon
        sid = request.GET['sid'] #get the id of the sermon
        Sermon = sermon.objects.get(id=sid) #get the sermon with the id received
        context["sdetails"] = Sermon #putting the sermon fetched into a list to pass it to the user

        #fetching comments for sermon
        SermonComments = comment.objects.filter(cfor=Sermon) #fetching comments for the sermon
        context['comments'] = SermonComments #putting comments in a context list

    else:
        #fetching all sermons
        allsermons = sermon.objects.all().filter(deleted=False) #fetching all sermons that have not been deleted
        if len(allsermons)>0: # if there are sermons in the database
            context["allsermons"] = allsermons #putting the sermons fetched into the context list
        else:
            context["nosermons"] = "There are no sermons..." #if there are no sermons show this message     
    return render(request,'sermons.html',context)




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