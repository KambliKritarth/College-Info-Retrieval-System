from django import forms
from .models import College, Post

class CollegeForm(forms.ModelForm):
	class Meta:
		model = College
		fields = ['course_id','region','clg_type','fees']

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','title_tag','author','body')

		widgets = {
			'title':forms.TextInput(attrs={'class':'form-control'}),
			'title_tag':forms.TextInput(attrs={'class':'form-control'}),
			'author':forms.TextInput(attrs={'class':'form-control','value':' ','id':'admin','type':'hidden'}),
			'body':forms.Textarea(attrs={'class':'form-control'}),
		}