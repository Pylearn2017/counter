from django.http import HttpResponse

def hello(request):
	global count
	count += 1
	return HttpResponse(f'<h1 align="center">You are visitor number {count} while the server is running</h1>')

count = 0	