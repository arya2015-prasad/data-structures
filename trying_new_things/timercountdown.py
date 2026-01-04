import time
class CountDownTimer:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def countDown(self):
        print(f"{self.hour} : {self.minute} : {self.second}")
        time.sleep(1)
        self.second -= 1
       
    def isAllZero(self):
        return self.hour == 0 and self.minute == 0 and self.second == 0 

    def adjustMinute(self):
        if self.second == 0:
            if self.minute > 0:
                self.minute -= 1
                self.second = 59
    
    def adjustHour(self):
        if self.minute == 0:
            if self.hour > 0:
                self.hour -= 1
                self.minute = 59
