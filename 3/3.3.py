# chapter 3.3
# Subject: loops
# Time: 2 minutes
# GO!

sum = 0
number =1
while(number < 13):
    sum+=number
    print(str(number)+ ' ) ' +str(sum))
    number+=1

tab = [5,10,15,1]
for x in range(0, len(tab)):
    print('poz: '+str(x)+ " Wartosc: "+str(tab[x]))

for x in range(len(tab)-2,-1,-1):
    print('poz: '+str(x)+ " Wartosc: "+str(tab[x]))
print(tab)