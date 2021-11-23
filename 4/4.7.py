# chapter 4.7
# Subject: methods
# Time: 2 minutes
# GO!

class Operations:
    c=13
    __priv=21

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def dsp(self):
        print(self.__priv)
        print(self.c)

op = Operations(5,2)
op.dsp()
print(op.c)
print(op.__priv)