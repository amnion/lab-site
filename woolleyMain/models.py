from django.db import models

# Create your models here.

class Publication(models.Model):
	authors = models.CharField(max_length = 1000)
	date = models.DateField()
	title = models.CharField(max_length = 1000)
	journal = models.CharField(max_length = 1000)
	link = models.URLField(max_length = 1000)

	def get_year(self):
		return self.date.year

class Person(models.Model):

	JOB_CHOICES = (
		('1', 'Principal Investigator'),
		('2', 'Post-doctoral Fellow'),
		('3', 'Graduate Student'),
		('4', 'Research Staff'),
		('5', 'Lab Alumni'),
		('6', 'Undergraduate Researcher'),
		('7', 'Former Undergraduate Researcher'),
		)

	name = models.CharField(max_length = 1000)
	job_status = models.CharField(max_length = 1000, choices = JOB_CHOICES, default = '3')
	description = models.CharField(max_length = 1000, blank = True)
	picture = models.ImageField(blank = True, default = 'woolleyMain/default_profile_pic.jpg')
	cv = models.FileField(blank = True)
	weblink = models.CharField(max_length = 1000, blank = True)
	email = models.CharField(max_length = 1000, blank = True)

class LabNewsItem(models.Model):

	header = models.CharField(max_length = 1000)
	text = models.CharField(max_length = 1000)
	date = models.DateField()

class LabMissionText(models.Model):

	text = models.CharField(max_length = 1000)

class ResearchItem(models.Model):

	text = models.CharField(max_length = 1000)
	picture = models.ImageField(blank = True)

class CommunityDescription(models.Model):

	text = models.CharField(max_length = 1000)