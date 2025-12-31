
num_dict = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six", 
    "7" : "seven",
    "8" : "eight",
    "9" : "nine",
    "10" : "ten",
    "11" : "eleven",
    "12" : "twelve",
    "13" : "thirteen",
    "14" : "fourteen",
    "15" : "fifteen",
    "16" : "sixteen",
    "17" : "seventeen",
    "18" : "eighteen",
    "19" : "nineteen",
    "20" : "twenty",
    "30" : "thirty",
    "40" : "fourty",
    "50" : "fifty",
    "60" : "sixty",
    "70" : "seventy",
    "80" : "eighty",
    "90" : "ninety",
    "100" : "hundred",
    "1000" : "thousand"
}

def ooo(n):
    return ""

def oon(n):
    if n[0] == '0' and n[1] == '0' and int(n[2]) > 0 : 
        return num_dict.get(n[2])
    return None 

def ono(n):
    if n[0] == '0' and int(n[1]) > 0 and n[2] == "0" :
        s = n[1] + n[2]
        return num_dict.get(s)
    return None

def onn(n): # 058
    if n[0] == '0' and int(n[1]) > 0 and int(n[2]) > 0 :
        s = n[1] + n[2] #58
        word = num_dict.get(s)
        if word == None : 
            word = ono("0"+ n[1]+ "0") +" "+ oon("00"+n[2]) #050 008
        return word
    return None

def noo(n):
    if int(n[0]) > 0 and n[1] == '0' and n[2] == "0":
        word = oon("00"+n[0]) + " hundred "            
        return word

def non(n):
    if int(n[0]) > 0 and n[1] == "0" and int(n[2]) > 0:
        word = noo(n[0] + "00") + oon("00" + n[0])
        return word

def nno(n):
    if int(n[0]) > 0 and int(n[1]) > 0 and n[2] == '0':
        word = noo(n[0] + "00") + ono('0' + n[1] + '0')
        return word

def nnn(n):
    if int(n[0]) > 0 and int(n[1]) > 0 and int(n[2]) > 0:
        w = noo(n[0] + "00") + onn('0' + n[1] + n[2])
        return w
    

def numToWord(n): 
    i = len(n) - 1
    j = 0
    arr = []

    while i >=0 :
        a = n[i]
        b = '0'
        c = '0'
        if i-1 >= 0:
            b = n[i-1]
        if i-2 >=0:
            c = n[i-2]
        arr.append(c + b + a)
        i -= 3
        j += 1
  

    k = len(arr) - 1
    ret = ''
    while k >= 0 :
        val = oon(arr[k])
        if val == None:
            val = ono(arr[k])
        if val == None:
            val = onn(arr[k])
        if val == None:
            val = noo(arr[k])
        if val == None:
            val = non(arr[k])
        if val == None:
            val = nno(arr[k])
        if val == None:
            val = nnn(arr[k])
        if val != None:
            ret += val
        if k == 3 :
            ret += " billion "    
        elif k == 2 :
            ret += " million "
        elif k == 1:
            ret += " thousand "
        
        k -= 1
    return ret
    
print(numToWord("318"))
print(numToWord("4335345"))


'''
num = input("Enter a number [1 to 1000]: ")

if num == 1:
    print(mydictionary["1"])

elif num == 2:
    print(mydictionary["2"])

elif num == 3:
    print(mydictionary["3"])

elif num == 4:
    print(mydictionary["4"])

elif num == 5:
    print(mydictionary["5"])

elif num == 6:
    print(mydictionary["6"])

elif num == 7:
'''