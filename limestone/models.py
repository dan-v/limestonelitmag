from django.db import models

# Create your models here.

STORY_CHOICES = (
	('Fiction', 'fiction'),
	('Poetry', 'poetry'),
	('Art', 'art'),
)

class Author(models.Model):
	author_name = models.CharField(max_length=32)

	def __unicode__(self):
		return self.author_name

class Issue(models.Model):
	overview = models.TextField()
	# issue_month = models.CharField(max_length=10, choices=MONTH_CHOICES)
	# issue_year = models.CharField(max_length=4, choices=YEAR_CHOICES)
	issue_date = models.DateField()
	display_name = models.CharField(max_length=20)
	latest_issue = models.BooleanField()
	active_issue = models.BooleanField()
	
	def __unicode__(self):
		return self.display_name
	
class Story(models.Model):
	issue = models.ForeignKey(Issue)
	headline = models.CharField(max_length=200, null=True, blank=True)
	content = models.TextField()
	story_type = models.CharField(max_length=7, choices=STORY_CHOICES)
	author = models.ForeignKey(Author)

	def __unicode__(self):
		return self.headline

class Headline(models.Model):
	quote = models.CharField(max_length=200, null=True, blank=True)
	active = models.BooleanField()
	author = models.ForeignKey(Author)

	def __unicode__(self):
		return self.quote
