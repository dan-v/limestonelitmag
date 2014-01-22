from django.shortcuts import render
from models import Story, Issue

# Create your views here.
from django.http import HttpResponse

def index(request):
	latest_story_list = Story.objects.order_by('-headline')[:5]
	latest_issue = Issue.objects.filter(latest_issue='True')
	context = {'latest_story_list': latest_story_list, 'latest_issue': latest_issue}
	return render(request, 'index.html', context)

def archives(request):
	return render(request, 'archive.html')

def about(request):
	return render(request, 'about.html')

def currentissue(request):
	latest_issue = Issue.objects.filter(latest_issue='True')
	latest_story_list = Story.objects.filter(issue=latest_issue)
	context = {'latest_issue': latest_issue, 'latest_story_list': latest_story_list}

	return render(request, 'currentissue.html', context)

def submit(request):
	return render (request, 'submit.html')
