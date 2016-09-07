from django.shortcuts import render, redirect
from django.template import Context
from login.models import Participant
import random
import logging

# Create your views here.

def index(request):
	question_set = [
		["ENCRYPTION", "CRYPTOGRAPHY", "DECIPHERING"],
		["VIRTUALIZATION", "MIDDLEWARE", "INTERCONNECTION"],
		["GRANULARITY", "MICROKERNEL", "SYNCHRONOUS"]
	]
	set_no = random.randint(0,2)
	context = Context({"questions": question_set[set_no], "set_no":set_no})
	return render(request, 'r1l2/index.html', context)


def exit(request):
	answer_set = [
		["XPXXHEPJ", "W@OKJO@O", "XOJXK@XOO"],
		["XHPK@OHE", "HWXK@XOX", "XF@O@HXJW"],
		["X@PKJPOF@", "XOEO@FJJ", "XFWXHPXK@"],
	]
	if request.session["finishedround2"] == False:
		set_no = request.POST["question_set"]
		p = Participant.objects.get(pk=request.session['userid'])
		for i in range(1,4):
			if request.POST["answer"+str(i)].upper() == answer_set[i-1]:
				p.score += 1

		p.save()
		request.session["finishedround2"] = True

	return render(request, 'r1l2/reaction.html')
