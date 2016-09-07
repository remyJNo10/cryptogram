from django.shortcuts import render

# Create your views here.

def index(request):
	question_set = [
		
	]
	set_no = random.randint(0,2)
	context = Context({"questions": question_set[set_no], "set_no":set_no})
	return render(request, 'r1l2/index.html', context)