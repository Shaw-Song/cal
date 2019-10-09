import calendar

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta, date
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar

class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('month',''))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month']=prev_month(d)
        context['next_month']=next_month(d)
        return context
def get_date(req_month):
    print(req_month)
    print("\n\nasdfasd\n")
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return date.today()
def prev_month(d):
    first = d.replace(day=1)
    prev_m = first - timedelta(days=1)
    month = 'month=' + str(prev_m.year)+'-'+str(prev_m.month)
    return month
def next_month(d):
    days_in_month = calendar.monthrange(d.year,d.month)[1]
    last = d.replace(day=days_in_month)
    next_m = last + timedelta(days=1)
    month = 'month=' + str(next_m.year)+'-'+str(next_m.month)
    return month



# Create your views here.

def index(request):
    return HttpResponse('hello')
