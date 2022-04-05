import pickle
from serializacja import Client

if __name__ == '__main__':
    c3 = Client("BL")
    pkFile = "tmp_pk"
    with open(pkFile, "wb") as fp:
        #c3p = pickle.Pickler(fp).dump(c3)
        print("zapis")
        c3p = pickle.dump(c3, fp)