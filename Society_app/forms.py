from django import forms
from .models import People


class PeopleForm(forms.ModelForm):
	class Meta:
		model = People
		fields = ('about_me', 'first_name', 'last_name', 'username', 'birth_date', 'fav_movies', 'photo_url')