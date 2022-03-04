#StringFormat method  --->strftime(paramater) this method uses formating Date Time fields
    # %y --> short year 22 ,    %Y-->full Year 2022
    # %b --> short month jan,   %B-->full month Januvary
    # %a --> short day sat,     %A-->full day satuarday
    # %w --> Number of week days (0-6)
    # %H --> full hours (24hrs),   %I-->small hours (12hrs)
    # %M  -->Minutes(0-59 mins)
    # %S  -->Seconds(0-59 sec)
    # %p (AM/Pm)
    # %f --> micro seconds (0000 to 9999)
    # %j --> Day number of year
#SYNTAX :  strftime("Formatting paramater %y")'''
import datetime
cd = datetime.datetime.now()
# %y --> short year 22
res = cd.strftime("%y")
print("short year:",res)
#%Y-->full Year 2022
res = cd.strftime("%Y")

# %b --> short month jan,
print("full year:",res)
res = cd.strftime("%b")
print("short month:",res)
# %B --> Full month januvary,
res = cd.strftime("%B")
print("full month:",res)
#%a-->short day fri
res = cd.strftime("%a")
print("half day:",res)
#%A-->full day friday
res = cd.strftime("%A")
print("full day:",res)
# %w --> Number of week days (0-6)
res = cd.strftime("%w")
print("Number of weeks:",res)
# %H --> full hours (24hrs)
res = cd.strftime("%H")
print("Hours 24:",res)
# %H --> full hours (24hrs)
res = cd.strftime("%I")
print("Hours 1 to 12:",res)

# %M  -->Minutes(0-59 mins)
res = cd.strftime("%M")
print("Minutes 0-59:",res)

# %S  -->Seconds(0-59 sec)
res = cd.strftime("%S")
print("seconds 0 to 59:",res)

# %p (AM/Pm)
res = cd.strftime("%p")
print("am or pm: ",res)

# %j --> Day number of Year
res = cd.strftime("%j")
print("Day number of year:",res)

#%x --> Date
res = cd.strftime("%x")
print("Only present date:",res)

# %X --> Time
res = cd.strftime("%X")
print("Time",res)













