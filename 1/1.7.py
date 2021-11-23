# chapter 1.7
# Subject: numbers
# Time: 6 minutes
# GO!

from math import *


name = "krystian"   # String
now = '2021'        # Sreing
age = 18            # Int
weight = 84.3       # Int (float)
isMale = True       # Bool
like = "Games"      # String
Streng = -100       # Int
hate = "PIS"        # String

print("My name is "+name)
print("I am Male "+str(isMale))
print("My weight is "+str(weight)+" at age "+str(int(now)-age))
print("Simple weight "+str(round(weight)))
print("True weight "+ str(ceil(weight)))
print("Fake weight "+str(floor(weight)))
print("\nI like "+like[0].lower()+like.replace(like[0],""))
print(type(like))
print("I hate "+hate+" with leng of ")
print(len(hate))
print(type(hate))