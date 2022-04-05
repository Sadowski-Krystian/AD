import io
import pickle

class Client:
    def __init__(self, name):
        self.ip = '192.168.0.1'
        self.host = 'teacherDesk'
        self.name = name
        print("jestem initem "+self.host+" dla "+self.name)

    def save(obj):
        return (obj.__class__, obj.__dict__)

    def load(cls, attr):
        obj = cls.__new(cls)
        obj.__dict__.update(attr)
        return obj

c1 = Client("GP")
print(c1)
print("")
c2 = Client("RR")
print(c2)
print("")

clp = pickle.dumps(c1)
print(clp)
c1 = None
print(c1)
c1 = pickle.loads(clp)
print(c1.host+" "+c1.name)
print(c1)
print("")

#Przepisać
c3 = Client("BL")
pkFile = "tmp_pk"
with open(pkFile, "wb") as fp:
#    c3p = pickle.Pickler(fp).dump(c3)
    c3p = pickle.dump(c3, fp)