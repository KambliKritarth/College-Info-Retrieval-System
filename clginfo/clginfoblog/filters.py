import django_filters

from .models import *

class ClgFilter(django_filters.FilterSet):
	class Meta:
		model = College
		fields = ['course_id', 'region', 'clg_type', 'fees']
