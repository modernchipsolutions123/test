import time;
#prints the number of ticks spent since
print(time.time())
print(time.localtime(time.time())) #It will display total date time
print(time.asctime(time.localtime(time.time()))) #It will display in accending order in time

for i in range(0,5):
    print(i)
    #Each element will be printed after 1 second
    time.sleep(2)
