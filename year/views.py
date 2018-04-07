from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import requests
# Create your views here
from .models import Test
from .forms import AddForm


def index(request):

	return render(request, 'yearbook/index.html')



def testform(request):
	if request.method == 'POST':
        # create a form instance and popuslate it with data from the request:
		form = AddForm(request.POST)
        # check whether it's valid:
		if form.is_valid():


			title = request.POST.get('title', '')
            # desc = request.POST.get('desc', '')
            # location = request.POST.get('location', '')
            # r = requests.get(
            #     "https://maps.googleapis.com/maps/api/geocode/json?address=" + location + "&key=AIzaSyCIXeZdC33t1bfnjdPKGmoVg5ebtT4ddNY")
            # json = r.json()
            # results = json['results']
            # latLng = {'lat': 25.2234975, 'lng': 73.7477857}
            # if(len(results) > 0):
            #     latLng = results[0]['geometry']['location']
            # {'lat': 25.2234975, 'lng': 73.7477857}
            # pic = request.FILES.get('pic', '')
            # comp_obj = Complaint(lat=latLng['lat'], lon=latLng['lng'], title=title, desc=desc, location=location,
            #                      pic=pic)
            # comp_obj.save()
			test_obj = Test(title = title)
			test_obj.save()

			return HttpResponseRedirect(reverse('home:index'))
	else:
		form = AddForm()
	
	context = {'form':form}


	return render(request, 'yearbook/post.html', context)