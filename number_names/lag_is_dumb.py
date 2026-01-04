class div:
    def __init__(self, D, d):
        self.D = D
        self.d = d
    
    def writeIfUserWantsWholeNumberVersionQuotient(self):
        WNVQ = self.D // self.d
        R = self.D % self.d
        return f"{self.D} divided by {self.d} is {WNVQ}. And the remainder is {R}."
    
    def writeIfUserWantsFloatVersionQuotient(self):
        Q = self.D / self.d
        return f"{self.D} divided by {self.d} is {Q}."

p1 = div(5, 2)
x = int(input("Options no.\n\n1. whole number quotient\n\n2. decimal number quotient\n\n"))
match x:
    case 1:
        print(p1.writeIfUserWantsWholeNumberVersionQuotient())
    case 2:
        print(p1.writeIfUserWantsFloatVersionQuotient())