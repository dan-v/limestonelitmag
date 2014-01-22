from django.shortcuts import render
from models import Story, Issue

# Create your views here.
from django.http import HttpResponse

def index(request):
	latest_issue = Issue.objects.filter(latest_issue='True', active_issue='True')
	latest_story_list = list(Story.objects.filter(issue=latest_issue).order_by('-headline')[:5])
	context = {'latest_story_list': latest_story_list, 'latest_issue': latest_issue}
	return render(request, 'index.html', context)

def archives(request):
	return render(request, 'archive.html')

def about(request):
	return render(request, 'about.html')

def currentissue(request):
	latest_issue = Issue.objects.filter(latest_issue='True', active_issue='True')
	latest_story_list_fiction = Story.objects.filter(issue=latest_issue, story_type='Fiction')
	latest_story_list_poetry = Story.objects.filter(issue=latest_issue, story_type='Poetry')
	context = {'latest_issue': latest_issue, 'latest_story_list_fiction': latest_story_list_fiction, 'latest_story_list_poetry': latest_story_list_poetry}

	return render(request, 'currentissue.html', context)

def submit(request):
	return render (request, 'submit.html')
