from django.http import HttpResponse

def hello(request):
	global count, color, flag
	if flag:
		if color <= 255:
			color += 5
		else:
			flag = False
	else: 	
		if color >= 0:
			color -= 5
		else:
			flag = True		
	count += 1
	return HttpResponse(
	f'<div style="background-color:rgb({color},{color},{color}); \
		width: 100%; \
		height: 100%"> \
			<h1 style="color:rgb({255-color},{255-color},{255-color});" align= "center">\
				You are visitor number {count} while the server is running\
			</h1>\
	</div>')

count = 0
color = 255	
flag = True