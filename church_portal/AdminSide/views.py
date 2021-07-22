from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from accounts.models import Customusers
from AdminSide.models import sermon
from django.contrib import messages
from django.db.models import Q

# Create your views here.
@login_required(login_url='login')
def admindash(request):
    return render(request,'adminhome.html')


@login_required(login_url='login')
def finance(request):
    return render(request,'adminfinances.html')


@login_required(login_url='login')
def sermons(request):
    context={}
    if request.method=="POST": #checking if a post request was received
        action = request.POST['action'] #getting the type of button that was clicked

        if action=="add sermon": #if user clicked the add new sermon button
            title = request.POST['title'] #get the sermon title entered by the user
            content = request.POST['content'] #get the content of the sermon entered by the user
            img = request.FILES['pic'] #get the image of the sermon uploaded by the user

            Sermon = sermon() 
            Sermon.title = title #setting new sermon title to the title entered entered by user
            Sermon.content = content #setting new sermon content to the content entered by user
            Sermon.image = img #setting new sermon image to the image uploaded by user
            Sermon.save() #saving the new sermon

            return redirect('/AdminSide/sermons/') #redirecting to the sermons page
    else:
        #fetching all sermons
        allsermons = sermon.objects.all() #fetching all sermons
        if len(allsermons)>0: # if there are sermons in the database
            context["allsermons"] = allsermons #putting the sermons fetched into the context list
        else:
            context["nosermons"] = "There are no sermons..." #if there are no sermons show this message     
    return render(request,'adminsermons.html',context)




@login_required(login_url='login')
def users(request):
    context={} #list to hold data

    if request.method=="POST": #checking if a post request was received
        action = request.POST['action'] #getting the type of button that was clicked
        
        if action=="new user": #if the user clicked the add new user button
            fname = request.POST['fname'] #get the first name entered by the user
            lname = request.POST['lname'] #get the last name entered by the user
            email = request.POST['email'] #get the email entered by the user
            password = request.POST['password'] #get the password entered by the user

            #checking if email is already registerd with another user
            if Customusers.objects.filter(email=email).exists(): #if email already exist in the database
                messages.info(request,"A user is already registered with this email") #message to the admin
            else:

                #registring the user
                user = Customusers()
                user.username = email #setting the username to the email entered
                user.email = email #setting the email to the email entered
                user.first_name = fname #settig the first name to the first name entered
                user.last_name = lname #setting the last name to the last name entered
                user.set_password(password) #setting the password to the password entered
                user.save() #saving user to the database
                messages.info(request,"An account has been created for " + fname +" "+lname) #message for the admin
                return redirect('/AdminSide/users/') #redirecting to the users page

        elif action=="search": #if search button is clicked
            squery = request.POST['searchquery'] #get the search query entered by the user
            if len(squery)>0: #if a search query was entered
                searchresults = Customusers.objects.filter(Q(first_name__icontains=squery) | Q(last_name__icontains=squery)).filter(is_active=True) #fetch all users with first name and last name matching the search query
                print(searchresults)
                if len(searchresults)>0: #if search results is not empty
                    context["allusers"] = searchresults #storing search results in the context list
                else: #if search result is empty
                    context["noresults"] = "No user matches search query "+"'"+squery+"'" #display this message
            else: #if no search query was entered
                context["nothingentered"] ="No search query entered"

    elif "uid" in request.GET: #if user clicks the edit icon
        uid = request.GET['uid'] #get the id of the user clicked on
        user = Customusers.objects.get(id=uid) #fetch all information of the user clicked on
        context["userdetails"] = user #putting the user information into a list
        

    elif "delid" in request.GET: #if user clicks the delete button
        delid = request.GET['delid'] #getting the id of user to delete
        user = Customusers.objects.get(id=delid) #getting the user to delete
        user.is_active = False #setting user to inactive status
        user.save() #saving the update
        messages.info(request,user.first_name +" "+user.last_name+" deleted!") #message to the admin
        return redirect('/AdminSide/users') #redirecting to the users page
        
    else:
        #fetching all church members in the database
        allusers = Customusers.objects.all().exclude(is_superuser=True).exclude(admin=True).filter(is_active=True)
        if len(allusers)>0: #if there are users in the database
            context["allusers"] = allusers #storing fetch results in the context list
        else: #if there are no users in the database
            context["nousers"] = "There are no registered users" #storing no results message in the context list

                
    return render(request,'adminusers.html',context)

