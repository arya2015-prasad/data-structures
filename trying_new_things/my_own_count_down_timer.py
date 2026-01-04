import time
class Timer:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def isTimeUp(self):
        return self.hour == 0 and self.minute == 0 and self.second == 0
    
    def cd(self):
        print(f"{self.hour} : {self.minute} : {self.second}")
        time.sleep(1)
        self.second -= 1
        if self.second == -1:
            if self.minute > 0:
                self.minute -= 1
                self.second = 59

                if self.minute == -1:
                    if self.hour > 0:
                        self.hour -= 1
                        self.minute = 59

timer = Timer(0, 1, 3)
while True:
  timer.cd()
  if timer.isTimeUp():
   
    print("Time is UP lil bro!")
    break

else:
 while True:
    timer.cd()