# chapter 4.2
# Subject: arguments
# Time: 2 minutes
# GO!

def sum(a,b=9):
    return a+b

print(sum(1))
print(sum(1,2))
print('')



def sum2(a,b=9):
    print('a='+str(a))
    print('b='+str(b))
    return a+b
print(sum2(1,2))
print('')
print(sum2(b=2,a=1))