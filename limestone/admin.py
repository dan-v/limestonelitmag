from django.contrib import admin
from limestone.models import Issue, Story, Author, Headline
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
	fields = ['author_name']

class HeadlineAdmin(admin.ModelAdmin):
	list_display = ('author', 'active')

class IssueAdmin(admin.ModelAdmin):
	fields = ['display_name', 'issue_month', 'issue_year', 'overview', 'latest_issue', 'active_issue']
	list_display = ('display_name', 'latest_issue', 'active_issue')

class StoryAdmin(admin.ModelAdmin):
	list_display = ('headline', 'issue', 'author', 'story_type')
	list_filter = ['issue', 'author', 'story_type']
	search_fields = ['headline', 'content']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Headline, HeadlineAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Story, StoryAdmin)