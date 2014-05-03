from datetime import date, time, datetime
from django.contrib.auth.models import User
from square.models import Volunteer, Event, EventLocation
import random, string

def timeonly_delta(time1, time2):
    start_date = dateize(time1)
    end_date = dateize(time2)
    return start_date-end_date


def dateize(time):
    return datetime.combine(date.today(), time)


def gen_password(length=8):
    myrg = random.SystemRandom()
    alphabet = string.ascii_letters + string.digits + string.punctuation
    pw = str().join(myrg.choice(alphabet) for c in range(length))
    return pw


def process_user(uname, pw, first, last):

	u = User.objects.create_user(
		first_name=first, 
		last_name=last, 
		password=pw, 
		username=uname)

	u.save()

	v = Volunteer(user=u)
	
	v.save()

	return v

	
#evt=event time, evl=event location, d=date, start=start time, end=end time, notes=notes, vt=is_volunteer_time
def process_event(evt, evl, d, start, end, notes, vt):
	
	e = Event(
	event_type=evt,
	event_location=EventLocation(evl),
	date=d,
	start=start,
	end=end,
	notes=notes,
	is_volunteer_time=vt)
	
	e.save()
	
	return(e)
		
		
    
def gen_username(first_name, last_name, date):
    return '{0}{1}:{2}'.format(
            first, last, v.signup_date.strftime('%m-%d-%y'))



