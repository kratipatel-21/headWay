from django.shortcuts import redirect, render, HttpResponseRedirect
from Wayahead.models import *
from django.contrib.auth import login,authenticate,logout
from Wayahead.forms import *

def Home(request):
    topics = Topic.objects.all()
    return render(request,'home.html', {'topics': topics})

def Queslist(request, topic):
    if request.user.is_authenticated:
        userobj = UserProfile.objects.get(user=request.user)
        if request.method =='POST':
            for key in request.POST:
                if 'status' in key:
                    if request.POST[key]=='review':
                        userobj.completed.remove(Question.objects.get(id= int(key.split('status_')[1])))
                        userobj.review.add(Question.objects.get(id=int (key.split('status_')[1])))
                    elif request.POST[key]=='completed':
                        userobj.review.remove(Question.objects.get(id= int(key.split('status_')[1])))
                        userobj.completed.add(Question.objects.get(id=int (key.split('status_')[1])))
                    else:
                        userobj.review.remove(Question.objects.get(id= int(key.split('status_')[1])))
                        userobj.completed.remove(Question.objects.get(id= int(key.split('status_')[1])))
            return HttpResponseRedirect('/question/'+ topic)
        else:
            questions = Question.objects.filter(topic =Topic.objects.get(topic=topic))

            return render(request,'queslist.html',{'questions': questions,'review':userobj.review.all(), 'completed': userobj.completed.all()})   #from chrome to us

    else:
        return HttpResponseRedirect('/login')





def UserLogin(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=LogIn(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username= uname, password= upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/')
        else:
            form=LogIn()          
            return render(request, 'login.html',{'form':form})
    else:
        return HttpResponseRedirect('/')

def Usersignup(request):
    if request.method=='POST':
        form=SignUp(request.POST)
        if form.is_valid(): 
            user=form.save()
    else :
        form=SignUp()
    return render(request, 'signup.html',{'form': form})


def ulogout(request):
    logout(request)
    return HttpResponseRedirect('/')


def profile(request):
    if request.user.is_authenticated:
        userobj=UserProfile.objects.get(user=request.user)
        completed=len(userobj.completed.all())
        review=len(userobj.review.all())
        not_seen=len(Question.objects.all())-review-completed
        total_points=0
        for question in userobj.completed.all():
            total_points=question.point + total_points
        return render(request, 'profile.html',{'completed': completed, 'review': review,'not_seen': not_seen, 'points':total_points})
    else:
        return HttpResponseRedirect('/login')




