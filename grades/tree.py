class Student:
    def __init__(self, name, eng, math, science, art):
        self.name = name
        self.eng = eng
        self.math = math
        self.science = science
        self.art = art
    
    def addMarks(self, sub, mark):
        if sub == "English":
            self.eng = mark

        if sub == "Math":
            self.math = mark
        
        if sub == "Science":
            self.science = mark
        
        if sub == "Art":
            self.art = mark
    
    def calc_grade(self):
        total = self.eng + self.math + self.science + self.art
        per = (total/400) * 100
            
        if per >= 90:
                return "A"
        elif per >= 80:
                return "B"
        elif per >= 70:
                return "C"
        elif per >= 50:
                return "D"
        else:
                return "F"

p1 = Student("Jasmine", 40, 56, 32, 89)
print(p1.calc_grade())
x = lambda a, b, c, d : (a + b + c + d)/400 * 100
print(x(40, 56, 32, 89))