import time

hour = 10
minute = 55
second = 2

while True:
    time.sleep(1)
    second += 1
    print(f"{hour} : {minute} : {second}")
    if second == 60:
        minute += 1
        second = 0
        if minute == 60:
            hour += 1
            minute = 0
            if hour == 24:
                hour = 0