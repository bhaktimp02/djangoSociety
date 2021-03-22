from django.urls import path
from . import views
from .views import PeopleView

app_name = "Society_app"

urlpatterns = [
	
	path('society/', views.index,name='index'),

	path('society/join/', PeopleView.as_view()),
	
	path('society/people/', views.UserView, name="userview"),

	path('society/group/', views.GroupView, name="groupview"),

	path('society/event/', views.EventView, name="eventview"),

	path('people/<int:article_id>/', views.UserDetail, name='userdetails'),

	path('group/<int:article_id>/', views.GroupDetail, name='groupdetails'),

	path('event/<int:article_id>/', views.EventDetail, name='eventdetails'),
	
]