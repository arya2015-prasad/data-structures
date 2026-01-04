from timercountdown import CountDownTimer

cdt = CountDownTimer(0, 2, 3)
if cdt.minute > 60 or cdt.minute < 0 or cdt.second > 60 or cdt.second < 0:
    print("Out of range [time]!")
while True:
 cdt.countDown()
 if cdt.isAllZero():
    print("Time is up!")
    break
 else:
    cdt.adjustMinute()
    cdt.adjustHour()