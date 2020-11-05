from django.shortcuts import render
from django.http import HttpResponse
from . import db_handle as DBH
import json


# Create your views here.
def logout(request):
	try:
		del request.session['username']
	except Exception as E:
		print(E)
	return index(request)

def index(request):
	if(request.method == "POST"):
		email = request.POST.get('email')
		pwd = request.POST.get('pass')
		print(email, "\t", pwd)
		get_Teachers = DBH.get_All_teachers()
		for t_id, t_name, t_email, t_pwd in get_Teachers:
			print(t_id, t_name, t_email, t_pwd)

		if(email == "harshit67@gmail.com" and pwd == "harshit@1996"):
			request.session['username'] = email
		else:
			message = {'msg': '-1'}
			return render(request, 'ar/login.html', {'msg': message})
	if(request.session.has_key("username")):
		data = {
			'email': request.session['username'],
			'pwd': "harshit@1996",
		}
		return render(request, 'ar/index.html', {'data': json.dumps(data)})
	return render(request, 'ar/login.html', {})
