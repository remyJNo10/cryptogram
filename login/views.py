from django.shortcuts import render, redirect
from login.models import Participant


# Create your views here.

def ShowLogin(request):
	return render(request, 'login/index.html')


def PerformLoginAction(request):
	participant_entity = Participant(participant_name=request.POST['participant_name'], college_name=request.POST['college_name'])
	participant_entity.save()
	request.session["user"]=request.POST['participant_name']
	return redirect('/landingpage/')
