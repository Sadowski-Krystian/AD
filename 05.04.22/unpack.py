import imp
import io
import pickle
from tkinter.messagebox import NO

if __name__ == '__main__':
    c3 = None
    print("zawartość zmiennej c3:")
    print(c3)
    print("")
    
    pkFile = 'tmp_pk'
    with open(pkFile, "rb") as fp:
        c3 = pickle.Unpickler(fp).load()
        #c3 = pickle.load(fp)

    print("zawartość zmiennej c3: ")
    print(c3.name)