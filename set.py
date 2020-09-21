
from datetime import datetime, timedelta
from time import time

#Add comments to the code where needed

def timestamp_demo():
    timestamp = time() # Number of ticks since 12:00am, January 1, 1970
    current_time = datetime.fromtimestamp(timestamp) # Datetime according to POSIX timestamp
    utc_datetime = datetime.utcfromtimestamp(timestamp) # Universal Coordinated time
    dt = datetime.fromisoformat('2018-11-30')
    print(current_time)
    # ISO format: YYYY-MM-DDTHH:MM:SS.ffffff

def main():
    setup = None
    long_ago = datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=5)
    day = timedelta(days=1)
    first_work_day = datetime(year=2018, month=11, day=5, hour=9, minute=0, second=0, microsecond=0, tzinfo=TZ_INFO())
    first_pay_day = datetime(year=2018, month=11, day=23, hour=17, minute=0, second=0, microsecond=0)
    assert first_work_day < first_pay_day
    delta_to_first_pay = first_work_day - first_pay_day
    two_weeks = timedelta(weeks=2)
    two_weeks = day * 14 
    next_pay_day = last_pay_day + two_weeks
    
    # You can add and subtract timedelta objects to data objects
    #This is a 'innovative feature' of the datetime module
    today = datetime.today()
    tomorrow = today + day
    yesterday = today - day
    
    #datetime.combine(date, time, tzinfo=self.tzinfo)
	#Return a new datetime object whose date components are equal to the given date object’s, 
	#and whose time components are equal to the given time object’s. 
    datec = date.today()
    #Hours,minutes,seconds,miliseconds, tzinfo, fold (0 or 1)
    timec = time(23,30,40,3115,None,fold=0)
    #No tzinfo; takes the one from timeC
    dtime = datetime.combine(datec,timec)
    print(dtime)
      
    dtime.replace(year=2012,hour=3)
    print(dtime)
    
    print("The day of the week is: " + str(dtime.weekday()))
    
    print(False or bool(dtime))

	dtdict = {dtime:'51', dtime.replace(year=1990) : '82'}
    print(dtdict)
    
    
    
if __name__ == '__main__':
    main()