from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event


class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(start_time__day=day)
		d = ''
		for event in events_per_day:
			# d += f'<li class="btn-open-popup" onclick=testfunc(this)><button class="btn-open-popup">{event.title}</button></li>'
			d += f'<li><a href="#" data-toggle="modal" data-target="#myModal{event.id}">{event.title}</a></li>'
			d += f'<div class="modal" id="myModal{event.id}" data-backdrop="static" data-keyboard="true">\
			 <div class="modal-dialog modal-xl modal-dialog-centered">\
			<div class="modal-content"><div class="modal-header">\
			<h2 class="modal-title">{event.title}</h2>\
			<button type="button" class="close" data-dismiss="modal">&times;</button></div>\
			<div class="modal-body">{event.description}</div>\
			<div class="modal-footer"></div></div></div></div>'


		if day != 0:
			return f"<td><span class='date'>{day}</span><ul>{d}</ul></td>"
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		cal += f'</table>'
		return cal
