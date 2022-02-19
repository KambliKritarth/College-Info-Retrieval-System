from django.urls import path
from .views import UserRegisterView
#from . import views
#from .views import Home, ArticleDetailView

urlpatterns = [
	path('register/', UserRegisterView.as_view(), name = 'register'),
     
]