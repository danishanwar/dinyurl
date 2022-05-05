from django.shortcuts import render, redirect
import uuid
from .models import origUrl
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, 'index.html')

def create(request):
	if request.method == 'POST':
		url = request.POST['link']
		if url != "":
			uid = str(uuid.uuid4())[:5]
			new_url = origUrl(link=url,uuid=uid)
			new_url.save()
			return HttpResponse(uid)
		else:
			uid = "none"
			return HttpResponse(uid)

def go(request, pk):
	url_details = origUrl.objects.get(uuid = pk)
	return redirect(url_details.link)