import time
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def increase(self):
     print(f"{self.hour} : {self.minute} : {self.second}")
     time.sleep(1)
     self.second += 1
     if self.second == 60:
            self.minute += 1
            self.second = 0
            if self.minute == 60:
                self.hour += 1
                self.minute = 0
                if self.hour == 24:
                    hour = 0

p1 = Time(11, 3, 0)
while True:
 p1.increase()