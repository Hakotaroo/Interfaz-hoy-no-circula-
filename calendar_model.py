import calendar
from datetime import datetime

class CalendarModel:
    def __init__(self):
        self.current_year = datetime.now().year
        self.current_month = datetime.now().month
    
    def get_calendar(self, year, month):
        return calendar.monthcalendar(year, month)
