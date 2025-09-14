import time

scrib = 0
timeCounter = 0
timeCounterMin = 0
timeCounterHou = 0
timeCounterDay = 0


while True:
    timeCounter += 1
    
    if scrib == 0:
        time.sleep(1)
        print(str(timeCounter) + ' sec.')
    elif scrib == 1:
        time.sleep(1)
        print(str(timeCounterMin) + ' min. ' + str(timeCounter) + ' sec.')
    elif scrib == 2:
        time.sleep(1)
        print(str(timeCounterHou) + ' hour. ' + str(timeCounterMin) + ' min. ' + str(timeCounter) + ' sec.')
    elif scrib == 3:
        time.sleep(1)
        print(str(timeCounterDay) + ' day. ' + str(timeCounterHou) + ' hour. ' + str(timeCounterMin) + ' min. ' + str(timeCounter) + ' sec.')
    
    if timeCounter == 59:
        timeCounter = 0
        timeCounterMin += 1
        scrib = 1
    elif timeCounterMin == 59:
        timeCounter = 0
        timeCounterMin = 0
        timeCounterHou += 1
        scrib = 2
    elif timeCounterHou == 23:
        timeCounter = 0
        timeCounterMin = 0
        timeCounterHou = 0
        timeCounterDay += 1
        scrib = 3