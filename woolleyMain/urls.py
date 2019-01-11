from django.urls import path

from . import views

app_name = 'woolleyMain'
urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),
	path('research/', views.ResearchView.as_view(), name='research'),
	path('publications/', views.PubsView.as_view(), name='pubs'),
	path('people/', views.PeopleView.as_view(), name='people'),
	path('community/', views.CommunityView.as_view(), name='community'),
	path('gallery/', views.GalleryView.as_view(), name='gallery'),
	path('positions/', views.PositionsView.as_view(), name='positions'),
]