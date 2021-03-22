from django.db import models

# Create your models here.
class People(models.Model):
	about_me = models.CharField(max_length=100)
	birth_date = models.DateField()
	fav_movies = models.CharField(max_length=100)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	username = models.CharField(max_length=30)
	photo_url = models.ImageField(upload_to="images/")


class Group(models.Model):
	name = models.CharField(max_length=50)
	members = models.CharField(max_length=50)
	description = models.CharField(max_length=50)
	category = models.CharField(max_length=50)
	website_url = models.URLField()
	creator_name = models.ForeignKey(People, on_delete = models.CASCADE)

class Event(models.Model):
	creator_name = models.ForeignKey(People, on_delete= models.CASCADE)
	description = models.CharField(max_length=50)
	start_time = models.TimeField()
	end_time = models.TimeField()
	location = models.CharField(max_length=50)
	event_title = models.CharField(max_length=50)


class Feed(models.Model):
	feed_type = models.TextField()
	total_likes = models.PositiveIntegerField()
	comments = models.CharField(max_length=100)
	content = models.TextField()


class UserInfo(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)