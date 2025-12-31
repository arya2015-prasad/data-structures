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

def eee():
    return ""

def oox(x):
   if x[0] == "0" and x[1] == "0" and int(x[2]) > 0:
    return num_dict.get(x[2])

print(oox("003"))

def oxo(x):
    if x[0] == "0" and int(x[1]) > 0 and x[2] == "0":
        s = x[1] + x[2]
        return num_dict.get(s)
    return None

print(oxo("030"))

def oxx(x):
    if x[0] == "0" and int(x[1]) > 0 and int(x[2]) > 0:
        s = x[1] + x[2]
        wf = num_dict.get(s)
        if wf == None:
            wf = oxo('0' + x[1] + '0') + " " + oox("00" + x[2])
        return wf
    return None

print(oxx("056"))

def xoo(x):
    if int(x[0]) > 0 and x[1] == "0" and x[2] == "0":
          wf =  oox("00" + x[0]) + " hundred"
          return wf

print(xoo("400"))

def xox(x):
    if int(x[0]) > 0 and x[1] == "0" and int(x[2]) > 0:
        wf = xoo(x[0] + "00") + " "+oox("00" + x[2])
        return wf

print(xox("304"))

def xxo(x):
    if int(x[0]) > 0 and int(x[1]) > 0 and x[2] == "0":
        wf = xoo(x[0] + "00") + " " + oxo('0' + x[1] + '0')
        return wf

print(xxo("450"))

def xxx(x):
    if int(x[0]) > 0 and int(x[1]) > 0 and int(x[2]) > 0:
        wf = xoo(x[0] + "00") + " " + oxo('0' + x[1] + '0') + " " + oox("00" + x[2])
        return wf

print(xxx('456'))