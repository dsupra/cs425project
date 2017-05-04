from django.shortcuts import render
from django.http import HttpResponse
from rain.models import Rain 

def index(request):
	# Construct a dictionary to pass to the template engine as its context.
	# Note the key boldmessage is the same as {{ boldmessage }} in the template!
	rg_list = Rain.objects.order_by('station_name')

	context_dict = {'rains': rg_list}
	# Return a rendered response to send to the client.
	# We make use of the shortcut function to make our lives easier.
	# Note that the first parameter is the template we wish to use.
	return render(request, 'rain/index.html', context=context_dict)