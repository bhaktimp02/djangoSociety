# def signup(request):
	
# 	if request.method == 'POST':
# 		userinfo = UserInfo(username = request.POST.get('username'),
# 				password = request.POST.get('password') )
# 		userinfo.save()

# 	return render(request,'Society_app/home.html')

	# if UserInfo.objects.get(id=userinfo.id):
	# 	return render(request,'Society_app/home.html')
	# else:
	# 	template = loader.get_template('Society_app/index.html')
	# 	return HttpResponse(template.render({"message":"Error!!"},request))


#return render(request,'Society_app/home.html', context)
			# PeopleDetail = People(about_me=request.POST.get['about_me'], 
			# 	first_name=request.POST.get['first_name'],
			#  	last_name=request.POST.get['last_name'],
			#  	username = request.POST.get['username'],
			#  	birth_date = request.POST.get['birth_date'],
			#  	fav_movies = request.POST.get['fav_movies'],
			#  	photo_url = request.FILES.get['photo_url'])
		 # 	PeopleDetail.save()

# 	#if PeopleDetail.id is not None:
		# template = loader.get_template('Society_app/home.html')
		# context = {

		# 		"message" : "Success!",
		# }
		#return HttpResponse("Hello World! ")
		#return HttpResponse(template.render(context, request))
		# else:
		# 	template = loader.get_template('covid_blog/success.html')
		# 	return HttpResponse(template.render({"message":"Error!!!"}, request))
	
		# else:
		# 	template = loader.get_template('Society_app/home.html')
		# 	return HttpResponse(template.render({"message":"Error!!!"}, request))

# def Groupno(request,article_id):
# 	return HttpResponse("There are %s groups in the Society!" % arcticle_id)