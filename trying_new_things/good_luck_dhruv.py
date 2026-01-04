import time
class C:
    def __init__(self, hour, minu, sec):
        self.hour = hour
        self.minu = minu
        self.sec = sec
    
    def countdown(self):
        print(f"{self.hour} : {self.minu} : {self.sec}")
        while self.hour > 0:
            while self.minu > 0:
                while self.sec > 0:
                    time.sleep(1)
                    self.sec -= 1
                self.minu -= 1
            self.hour -= 1
        print("time is up!")

p1 = C(1, 1, 1)
p1.countdown()