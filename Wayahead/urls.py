from django.urls import path
from Wayahead.views import*

urlpatterns = [
    path('',Home),
    path('question/<str:topic>',Queslist),
    path('login',UserLogin),
    path('signup',Usersignup),
    path('logout',ulogout),
    path('p',profile),
]