class Employee:
    def __init__(self, name):
        self.name = name
        self.__salary = 3554
    
    def set_salary(self):
        if 10000 < self.__salary <= 300000:
            return "Access granted"

        else:
            return "Salary out of range"
               
    
    def get_salary(self):
        return self.__salary
    
    def check_salary_status(self):
        if self.__salary >= 100000:
            return "You must be too rich!"
        
        if self.__salary < 100000:
            return "You must be little too rich!"
        
        elif self.__salary <= 30000:
            return "You earn so less salary"
        
        elif self.__salary <= 60000:
            return "You earn an average amount of salary"
        
        else:
            return "Salary is out of range!"

p1 = Employee("Angutang")
print(p1.set_salary())
print(p1.get_salary())
print(p1.check_salary_status())