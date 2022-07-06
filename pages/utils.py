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
			d += f'<li><a href="#myModal{event.id}" data-bs-toggle="modal">{event.title}</a></li>'

			d += f'<div class="modal fade" id="myModal{event.id}" tabindex="-1" aria-labelledby="myModal{event.id}" aria-hidden="true">\
			    <div class="modal-dialog modal-dialog-centered">\
			        <div class="modal-content">\
			            <div class="modal-body p-5">\
			                <div class="text-center mb-4">\
			                    <h5 class="modal-title" id="staticBackdropLabel">{event.title}</h5>\
			                </div>\
			                <div class="position-absolute end-0 top-0 p-3">\
			                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>\
			                </div>\
			                <div class="mb-3">\
			                    <label for="nameControlInput" class="form-label">일시</label>\
			                    <input type="date" class="form-control" id="dateControlInput" value="{event.start_time}">\
			                </div>\
			                <div class="mb-3">\
			                    <label for="messageControlTextarea" class="form-label">세부일정</label>\
			                    <textarea class="form-control" id="messageControlTextarea" rows="4" placeholder="{event.description}"></textarea>\
			                </div>\
			                <div class="mb-4">\
			                    <label class="form-label" for="inputGroupFile01">Resume Upload</label>\
			                    <input type="file" class="form-control" id="inputGroupFile01">\
			                </div>\
			                <div class="mb-3">\
			                    <label for="emailControlInput2" class="form-label">담당자</label>\
			                    <input type="text" class="form-control" id="emailControlInput2" readonly="readonly" placeholder="{event.charge}">\
			                </div>\
			                    <button type="submit" class="btn btn-primary w-30 right">수정</button>\
			                    <button type="submit" class="btn btn-primary w-30 right">삭제</button>\
			            </div>\
			        </div>\
			    </div>\
			</div>'


			# d += f'<div class="modal fade" id="myModal{event.id} "tabindex="-1" aria-labelledby="myModal{event.id}" aria-hidden="true">\
			#  <div class="modal-dialog modal-dialog-centered">\
			# <div class="modal-content"><div class="modal-header">\
			# <h2 class="modal-title">{event.title}</h2>\
			# <button type="button" class="close" data-dismiss="modal">&times;</button></div>\
			# <div class="modal-body">{event.description}</div>\
			# <div class="modal-footer"></div></div></div></div>'


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
