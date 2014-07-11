from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from townsquare.forms import EventForm, VolunteerForm, LoginForm
from townsquare.models import Volunteer, Event
from townsquare.processing import process_valid_event_post,         \
        process_valid_volunteer_post, process_valid_login_post, \
        process_volunteer_get, process_event_get


def about(request):
    
    blurb = "Something about Townsquare."
    return render(request, 'users/about.html', 
                    {'blurb': blurb,})


def t2login(request):

    # POST request to login page does validation/processing
    form = LoginForm(request.POST)
    
    if form.is_valid():
        
        # authenticate the form
        succeeded = process_valid_login_post(request, form)
        if succeeded:
            return HttpResponseRedirect('/townsquare/volunteer/home')
        else:
            return HttpResponseRedirect('/townsquare/login')
    
    # render result of an invalid POST or a GET request
    return render(request, 'users/login.html', 
                    {'f': LoginForm()})


@login_required
def t2logout(request):
    
    logout(request)
    return HttpResponseRedirect('/townsquare/login')


@login_required 
def home(request):

    try:
        va = Volunteer.objects.get(id=request.user.volunteer.id) 
        return render(request, 'users/index.html',
                        {'va': va})

    # TODO: remove this try-except block; but wait until admin console
    #       is fully functional
    except Volunteer.DoesNotExist:
        return HttpResponseRedirect('/townsquare/volunteer/browse')
    

@login_required
def add_volunteer(request):
    if request.method == 'POST':
        
        # POST request to add_volunteer page does validation/processing
        form = VolunteerForm(request.POST)

        if form.is_valid():

            process_valid_volunteer_post(form)
            return HttpResponseRedirect('/townsquare/volunteer/browse')

    else:
        # GET request to add_volunteer page displays an empty form
        form = VolunteerForm()

    return render(request, 'users/add_volunteer.html', 
                    {'f': form})


@login_required
def edit_volunteer(request, vol_id):

    if request.method == 'POST':

        # POST request to add_volunteer page does validation/processing
        form = VolunteerForm(request.POST)

        if form.is_valid():

            process_valid_volunteer_post(form, int(vol_id))
            return HttpResponseRedirect('/townsquare/volunteer/browse')

    else:

        # GET request to edit_volunteer has to load the data properly
        form = process_volunteer_get(vol_id)
        
    # render an HTTP response if it was an invalid POST, or a GET
    return render(request, 'users/edit_volunteer.html', 
                    {'f': form, 'vol_id': vol_id})


@login_required
def browse_volunteers(request):
    
    vols = Volunteer.objects.all()
    return render(request, 'users/browse_volunteers.html',
                    {'volunteers': vols,})
    
        
@login_required
def add_event(request):

    # POST request does processing
    if request.method == 'POST':

        form = EventForm(request.POST)

        if form.is_valid():

            process_valid_event_post(form)
            return HttpResponseRedirect('/townsquare/event/browse')

    else:
        # GET request sends an empty form
        form = EventForm()

    # render an HTTP response if it was a GET, or an invalid POST
    return render(request, 'users/add_event.html', 
                    {'f': form})


@login_required
def edit_event(request, event_id=None):

    if request.method == 'POST':

        form = EventForm(request.POST)

        if form.is_valid():

            process_valid_event_post(form, event_id)
            return HttpResponseRedirect('/townsquare/event/browse')

    else:

        form = process_event_get(event_id)
        return render(request, 'users/edit_event.html',
                        {'f': form})

    # render an HTTP response if it was a GET, or an invalid POST
    return render(request, 'users/edit_event.html', 
                    {'f': form})


@login_required
def browse_events(request):
    evs = Event.objects.all()
    return render(request, 'users/browse_events.html',
                    {'events': evs,})


@login_required
def add_session(request):
	
	# POST request does processing
    if request.method == 'POST':

        form = SessionForm(request.POST)

        if form.is_valid():

		#As it stands, probably just going to bounce to the event browse, though the browse should eventually contain session data.

            process_valid_event_post(form)
            return HttpResponseRedirect('/townsquare/event/browse')

    else:
        # GET request sends an empty form
        form = SessionForm()

    # render an HTTP response if it was a GET, or an invalid POST
    return render(request, 'users/add_session.html', 
                    {'f': form})


@login_required
def edit_session(request, event_id=None):
	
	#Viewing info on vols who attended event
	#pass
	
	return render(request, 'users/edit_session.html')




    
@login_required
def browse_sessions(request):
	sesh = Session.objects.all()
	return render(request, 'users/browse_sessions.html',
                    {'sessions': sesh,})    

