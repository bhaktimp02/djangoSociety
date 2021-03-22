from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.urls import reverse

from .models import People, Group, Event, Feed, UserInfo
from .forms import PeopleForm

from django.views import View

# Create your views here.


def index(request):

	template = loader.get_template('Society_app/home.html')
	return HttpResponse(template.render({},request))


class PeopleView(View):
	form_class = PeopleForm
	initial = {'key' : 'value'}
	template_name = 'Society_app/join.html'

	def get(self, request, *args, **kwargs):
		form = self.form_class(initial=self.initial)
		return render(request,self.template_name,{'form':form})


	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponse("Successfully Signed Up")

		return render(request,self.template_name,{'form':form})


def UserView(request):	
	userview_list = People.objects.all()

	template = loader.get_template('Society_app/people.html')
	context = {
		'userview_list' : userview_list
	}

	return HttpResponse(template.render(context,request))
	


def GroupView(request):	
	groupview_list = Group.objects.all()


	template = loader.get_template('Society_app/group.html')
	context = {
		'groupview_list' : groupview_list
	}

	return HttpResponse(template.render(context,request))


def EventView(request):	
	eventview_list = Event.objects.all()

	template = loader.get_template('Society_app/event.html')
	context = {
		'eventview_list' : eventview_list
	}

	return HttpResponse(template.render(context,request))


def UserDetail(request, article_id):
	
	userdetails = People.objects.get(id=article_id)
	
	
	template = loader.get_template('Society_app/userdetails.html')
	context = {
		'userdetails' : userdetails,
		
	}
	return HttpResponse(template.render(context,request))
	

def GroupDetail(request, article_id):
	
	groupdetails = Group.objects.get(id=article_id)
	people = People.objects.get(id = article_id)
	
	template = loader.get_template('Society_app/groupdetails.html')
	context = {
		'groupdetails' : groupdetails,
		'people' : people
	}
	return HttpResponse(template.render(context,request))


def EventDetail(request, article_id):
	
	eventdetails = Event.objects.get(id=article_id)
	people = People.objects.get(id = article_id)
	
	template = loader.get_template('Society_app/eventdetails.html')
	context = {
		'eventdetails' : eventdetails,
		'people' : people
		
	}
	return HttpResponse(template.render(context,request))
	