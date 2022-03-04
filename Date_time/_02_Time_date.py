'''
import time;
t1 = time.localtime(time.time()) #It will display total time with mins,sec,hour,date ,month ,year
print("It will display total time with mins,sec,hour,date ,month ,year:",t1)
t1 = time.asctime(time.localtime(time.time())) #It will print only present time
print("It will print only present time:",t1)
#StringFormat method  --->strftime(paramater) this method uses formating Date Time fields
    # %y --> short year 22 ,    %Y-->full Year 2022
    # %w --> short month jan,   %W-->full month Januvary
    # %a --> short day sat,   %A-->full day satuarday
    # %H --> full hours (24hrs),   %I-->small hours (12hrs)
    # %M  -->Minutes(0-59 mins)
    # %S  -->Seconds(0-59 sec)
    # %p (AM/Pm)
    #%f --> micro seconds (0000 to 9999)
#SYNTAX :  strftime("Formatting paramater %y")'''

import datetime
res = datetime.datetime.now()
#Create a new date time by using this datetime() Constructor
res2 = datetime.datetime(2022,7,24)
#print(res)
print(res2.strftime("%D/%B/%Y"))


