#from django.urls import path
from . import views
from .views import Home, ArticleDetailView, FormView, DisplayView, EXTCView, OneLacFeesView, TwoLacFeesView,BelowOneLacFeesView, East, North, South, West, Autonomous, NonAutonomous, MechView, CivilView, InfoView, AddPostView
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    #path('',views.home,name="home"),
    path('',Home.as_view(),name="home"),
    path('article/<int:pk>',ArticleDetailView.as_view(),name='article-detail'),
    #path('filter',views.filter,name='filter'),
    path('display',DisplayView.as_view(),name='display'),
    path('cse',views.displaycse,name='cse'),
    path('extc',EXTCView.as_view(),name='extc'),
    path('mech',MechView.as_view(),name='mech'),
    path('civi',CivilView.as_view(),name='civi'),
    path('info',InfoView.as_view(),name='info'),
    path('fees_one_lac',OneLacFeesView.as_view(),name='fees_one_lac'),
    path('fees_two_lacs',TwoLacFeesView.as_view(),name='fees_two_lacs'),
    path('below_one_lac',BelowOneLacFeesView.as_view(),name='below_one_lac'),
    path('east',East.as_view(),name='east'),
    path('west',West.as_view(),name='west'),
    path('south',South.as_view(),name='south'),
    path('north',North.as_view(),name='north'),
    path('contact',views.contact,name = 'contact'),
    path('autonomous',Autonomous.as_view(),name = 'autonomous'),
    path('non-autonomous',NonAutonomous.as_view(),name = 'non-autonomous'),
    path('add_post',AddPostView.as_view(),name = 'add_post'),
    ]