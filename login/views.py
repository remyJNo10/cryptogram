from django.shortcuts import render, redirect
from login.models import Participant
import logging

# Create your views here.

def ShowLogin(request):
	return render(request, 'login/index.html')


def PerformLoginAction(request):
	if request.POST['participant_name']=="Username" or request.POST['college_name']=="University/College":
		return redirect("/")
	participant_entity = Participant(participant_name=request.POST['participant_name'], college_name=request.POST['college_name'])
	participant_entity.save()
	request.session["user"]=request.POST['participant_name']
	request.session["userid"]=participant_entity.id;
	request.session["finishedround1"]=False
	request.session["finishedround2"]=False
	print (request.session["userid"])
	return redirect('/round1/')
