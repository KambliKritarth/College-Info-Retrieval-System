from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse 
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, College, Contact
from .filters import ClgFilter
from .forms import CollegeForm, PostForm
from django.db.models import Q
#from .models import Snippet
from django.views import View
# Create your views here.
'''def home(request):
	return render(request,'home.html',{})'''
def display(request):
	colleges = College.objects.filter(clg_type = 'Autonomous')
	
	return render(request,'display.html')

def displaycse(request):
	colleges = College.objects.all()
	return render(request,'cse.html',{'college':colleges})

def displayextc(request):
	colleges = College.objects.all()
	return render(request,'extc.html',{'college':colleges})

def contact(request):
	model = Contact
	all_contacts = Contact.objects.all
	name = request.POST.get('name',"Anonymous")
	user_contact = request.POST.get('contact',"Contactless")
	user_query = request.POST.get('query',"Queryless")

	error_message = None

	if(not name):
		error_message = "Name is required"
	elif len(name) > 25:
		error_message = "Name cannot be more than 25 characters please try to use initials"
	elif len(user_query) > 500:
		error_message = "Query cannot be more than 500 characters please try to keep it short"
	elif user_contact.find("@") == -1 or user_contact.find(".") == -1 :
		error_message = "Invalid email address"	


	if not error_message:
		ins = Contact(name=name,contact = user_contact,query = user_query)
		ins.save()
		#print(name)
		return render(request, 'contact.html')
	else:
		return render(request, 'contact.html',{'error':error_message})
        


class Home(ListView):
	model = Post
	template_name = 'home.html'

class BelowOneLacFeesView(ListView):
	model = College 
	template_name = 'below_one_lac.html'

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	#fields = '__all__'


class FormView(ListView):
	model = Post
	template_name = 'filter.html'

class DisplayView(ListView):
	model = College 
	template_name = 'display.html'

class EXTCView(ListView):
	model = College 
	template_name = 'extc.html'

class MechView(ListView):
	model = College 
	template_name = 'mech.html'

class CivilView(ListView):
	model = College 
	template_name = 'civi.html'

class InfoView(ListView):
	model = College 
	template_name = 'info.html'

class OneLacFeesView(ListView):
	model = College 
	template_name = 'fees_one_lac.html'

class TwoLacFeesView(ListView):
	model = College 
	template_name = 'fees_two_lacs.html'

class East(ListView):
	model = College 
	template_name = 'east.html'

class North(ListView):
	model = College 
	template_name = 'north.html'

class West(ListView):
	model = College 
	template_name = 'west.html'

class South(ListView):
	model = College 
	template_name = 'south.html'

class Autonomous(ListView):
	model = College 
	template_name = 'autonomous.html'

class NonAutonomous(ListView):
	model = College 
	template_name = 'non-autonomous.html'

	#"Region":request.POST["regions"],
	#"Autonomy":request.POST["Autonomy"],
	#"CourseID":request.POST["CourseID"]	
	#print(Fees)
	'''clgs = displaycolleges.order_set.all()
	clg_count = clgs.count()'''

	