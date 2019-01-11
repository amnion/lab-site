from django.shortcuts import render
from django.views import generic

from django.http import HttpResponse

from .models import Publication, Person, LabNewsItem, LabMissionText, ResearchItem, CommunityDescription

# Create your views here.

class HomeView(generic.TemplateView):
	template_name = 'woolleyMain/home.html'
	
	def get_context_data(self):
		context = {
			'news_text_list': LabNewsItem.objects.order_by('-date'),
			'mission_statement': LabMissionText.objects,
		}
		return context

class ResearchView(generic.TemplateView):
	template_name = 'woolleyMain/research.html'

class PubsView(generic.ListView):
	template_name = 'woolleyMain/pubs.html'
	context_object_name = 'pub_list'

	def get_queryset(self):
		return Publication.objects.order_by('-date')

class PeopleView(generic.TemplateView):
	template_name = 'woolleyMain/people.html'

	def get_context_data(self):
		context = {
			'person_list': Person.objects.order_by('job_status'),
			'job_set': set(list([i['job_status'] for i in Person.objects.values('job_status')])), # janky way to get unique set of job values
		}
		return context

class CommunityView(generic.TemplateView):
	template_name = 'woolleyMain/community.html'

class GalleryView(generic.TemplateView):
	template_name = 'woolleyMain/gallery.html'

class PositionsView(generic.TemplateView):
	template_name = 'woolleyMain/positions.html'