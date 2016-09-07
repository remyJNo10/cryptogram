from django.shortcuts import render, redirect
from django.http import *
from django.template import Context
from login.models import Participant
import random
import logging

# Create your views here.


def index(request):
	question_set = [
		["œŒ@^#É@µÒ¼ñŒ@@¢Å@œ^œŒ@Å$@µ^@", "øÐ$œÉ%@øµ~ÐÉ$^œŒ@ìÐ¢¥", "Ð%@»µ%^œ$µ^Œ‰^µ%ÐœŒ@$»µ%^œ$@µ^É$@", "Ò@@€¼ÐÉ$ø$‰@%¥^¶¢Ð^@µ%¥¼ÐÉ$@%@»‰@^¶¢Ð^@$", "µ¢¢ÅÐÐ¥œŒ‰%Å^»É^œúÐ»@œÐµ%@%¥"],
		["€@Ð€¢@ñŒÐ¢‰~@‰%Å¢µ^^ŒÐÉ^@^ŒÐÉ¢¥%ÐœœŒ$Ðñ^œÐ%@^", "µ¶Œµ‰%‰^Ð%¢¼µ^^œ$Ð%Åµ^‰œ^ñ@µÒ@^œ¢‰%Ò", "¥Ð%Ðœ¶ÐÉ%œ¼ÐÉ$¶Œ‰¶Ò@%^ì@øÐ$@œŒ@¼Œµœ¶Œ", "Ì@œœ@$¢µœ@œŒµ\%\%@~@$", "Ì@µÉœ¼‰^‰%œŒ@@¼@ÐøœŒ@ì@ŒÐ¢¥@$"],
		["ŒÐ€@øÐ$œŒ@ì@^œìÉœ€$@€µ$@øÐ$œŒ@ñÐ$^œ", "¼ÐÉ¶µ%œ»µÒ@µ%Ð»@¢@œñ‰œŒÐÉœì$@µÒ‰%Åµø@ñ@ÅÅ^", "µñµœ¶Œ@¥€Ðœ%@~@$ìÐ‰¢^", "¥Ð%œì‰œ@œŒ@Œµ%¥œŒµœø@@¥^¼ÐÉ", "ÅÐÐ¥œŒ‰%Å^¶Ð»@œÐœŒÐ^@ñŒÐñµ‰œ"]
	]
	set_no = random.randint(0,2)
	context = Context({"questions": question_set[set_no], "set_no":set_no})
	return render(request, 'r1l1/index.html', context)
	


def verify(request):
	print("enters")
	answer_set = [
		["THE SQUEAKY WHEEL GETS THE GREASE",
		 "FORTUNE FAVOURS THE BOLD",
		 "ONE MANS TRASH IS ANOTHER MANS TREASURE",
		 "KEEP YOUR FRIENDS CLOSE AND YOUR ENEMIES CLOSER",
		 "ALL GOOD THINGS MUST COME TO AN END"
		],
		["PEOPLE  WHO LIVE IN GLASS HOUSE SHOULD NOT THROW STONES",
		 "A CHAIN IS ONLY AS STRONG AS ITS WEAKEST LINK",
		 "DO NOT COUNT YOUR CHICKENS BEFORE THEY HATCH",
		 "BETTER LATE THAN NEVER",
		 "BEAUTY IS IN THE EYE OF THE BEHOLDER"
		],
		["HOPE FOR THE BEST BUT PREPARE FOR THE WORST",
		 "YOU CANT MAKE AN OMELET WITHOUT BREAKING A FEW EGGS",
		 "A WATCHED POT NEVER BOILS",
		 "DONT BITE THE HAND THAT FEEDS YOU",
		 "GOOD THINGS COME TO THOSE WHO WAIT"
		]
	]
	if request.session["finishedround1"] == False:
		set_no = request.POST["question_set"]
		#print("set no is " ,set_no)
		p = Participant.objects.get(pk=request.session['userid'])
		#print("first: ", request.POST["answer"+str(1)].upper())
		#print("second: ", answer_set[int(set_no)][1-1])
		for i in range(1,6):
			print("index is ", i)
			if request.POST["answer"+str(i)].upper()  == answer_set[int(set_no)][i-1]:
				p.score += 1
		
		p.save()
		request.session["finishedround1"] = True
	
	return redirect('/round2/')



		