from django.shortcuts import render
from models import Story, Issue, Headline, Author

# Create your views here.
from django.http import HttpResponse

def index(request):
	latest_issue = Issue.objects.filter(latest_issue='True', active_issue='True')
	latest_story_list = list(Story.objects.filter(issue=latest_issue).order_by('-headline')[:5])
	context = {'latest_story_list': latest_story_list, 'latest_issue': latest_issue}
	return render(request, 'index.html', context)

def archives(request):
	archived_issues = Issue.objects.filter(latest_issue='False', active_issue='True')
	context = {'archived_issues': archived_issues}
	return render(request, 'archive.html', context)

def issue(request, number):
	issue = Issue.objects.filter(id=number)
	story_list_fiction = Story.objects.filter(issue=issue, story_type='Fiction')
	story_list_poetry = Story.objects.filter(issue=issue, story_type='Poetry')
	context = {'issue': issue, 'story_list_fiction': story_list_fiction, 'story_list_poetry': story_list_poetry}
	return render(request, 'issue.html', context)	

def about(request):
	author_list = Author.objects.order_by('author_name')
	context = {'author_list': author_list}
	return render(request, 'about.html', context)

def base(request):
	last_three_issues = Issue.objects.order_by('-issue_date')[:3]
	context = {'last_three_issues': last_three_issues}
	return render(request, 'base.html', context)

def submit(request):
	return render (request, 'submit.html')
