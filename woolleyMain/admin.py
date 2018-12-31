from django.contrib import admin

from .models import Publication, Person, LabNewsItem, LabMissionText, ResearchItem, CommunityDescription

# Register your models here.

admin.site.register(Publication)
admin.site.register(Person)
admin.site.register(LabNewsItem)
admin.site.register(LabMissionText)
admin.site.register(ResearchItem)
admin.site.register(CommunityDescription)