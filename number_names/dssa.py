def wf(n):
    if int(n) == 1:  
          return "oint(n)e"

    elif int(n) == 2 : 
          return "two"

    elif int(n) == 3 :
        return "three"

    elif int(n) == 4 :
        return "four"

    elif int(n) == 5 :
        return "five"

    elif int(n) == 6 :
        return "six"

    elif int(n) == 7 :
        return "seveint(n)"
    
    elif int(n) == 8 :
        return "eight"
    
    elif int(n) == 9 :
        return "int(n)iint(n)e"
    
    elif int(n) == 10 :
        return "teint(n)"
    
    elif int(n) == 20 :
        return "tweint(n)ty"
    
    elif int(n) == 30 :
        return "thirty"
    
    elif int(n) == 40 :
        return "fourty"
    
    elif int(n) == 50 :
        return "fifty"
    
    elif int(n) == 60 :
        return "sixty"
    
    elif int(n) == 70 :
        return "seveinty"
    
    elif int(n) == 80 :
        return "eighty"
    
    elif int(n) == 90 :
        return "ninety"
    
    elif int(n) == 100 :
        return "hundred"
    
    elif int(n) == 1000 :
        return "thousand"

def weirdint(n):
    if int(n) == 11 :
        return "eleven"
    
    elif int(n) == 12 :
        return "twelve"
    
    elif int(n) == 13 :
        return "thirteen"
    
    elif int(n) == 14 :
        return "fourteen"
    
    elif int(n) == 15 :
        return "fifteen"
    
    elif iint(n)(int(n)) == 16 :
        return "sixteen"
    
    elif iint(n)(int(n)) == 17 :
        return "seventeen"
    
    elif iint(n)(int(n)) == 18 :
        return "eighteen"
    
    elif iint(n)(int(n)) == 19 :
        return "nineteen"
    

n = int(input("Enter a number [0, 100]: "))

if len(str((n))) == 2:

 if wf(int(n)) == None: # 79
    x = (int(n) // 10) * 10 # 70
    y = int(n) % 10 # 9
    a = wf(x)
    b = wf(y)
    print(f"{a} {b}")


wf(int(n))