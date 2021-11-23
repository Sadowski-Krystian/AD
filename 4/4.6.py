# chapter 4.4
# Subject: methods
# Time: 2 minutes
# GO!

class Operations:
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.c=13
        self.__priv = 21
        

    def sum(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b
        
    def multiply(self,a,b):
        return a*b

    def div(self,a,b):
        return a/b
    
    def dsp(self):
        return self.c

op = Operations(5,2)

print(op.sum(5,2))
print(op.sub(1,2))
print(op.multiply(1,2))
print(op.div(1,2))
print(op.dsp())
