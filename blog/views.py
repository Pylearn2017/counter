from django.shortcuts import render
from time import strftime

def week_duty():
	number_of_week = strftime('%W')
	names_list = ['Александр', 'Динар', 'Ренат', 'Николай', 'Ольга',]
	number_of_week = int(number_of_week)
	i = number_of_week % len(names_list)
	name = names_list[i]
	return name


def data():
	day = strftime('%d.%m.%Y')
	return day

# Create your views here.
def posts_list(request):
	name = week_duty().upper()
	day = data()
	return render(request, 'blog/index.html', context = {'name' : name, 'data' : day})

data()