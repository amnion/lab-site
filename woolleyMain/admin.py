from django.contrib import admin

from .models import Publication, Person, LabNewsItem, LabMissionText, ResearchItem, CommunityDescription

class PersonAdmin(admin.ModelAdmin):
	list_display = ('name', 'job_status')
	list_filter = ['job_status']

class PubAdmin(admin.ModelAdmin):
	list_display = ('title', 'date', 'journal')
	ordering = ('-date',)

class NewsAdmin(admin.ModelAdmin):
	list_display = ('header', 'date')
	ordering = ('-date',)

admin.site.register(Publication, PubAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(LabNewsItem, NewsAdmin)
admin.site.register(LabMissionText)
admin.site.register(ResearchItem)
admin.site.register(CommunityDescription)