import io
import pickle
import copy

class Cos:
    attr = 'Atrybut klasy'

print("Klasa Cos z inicjacji cos:")
print(Cos)
print(Cos.attr)
print("")
pkcos = pickle.dumps(Cos)
print(pkcos)
print("")
thing = pickle.loads(pkcos)
print("klaca cos z instancją thing:")
print(thing)
print(thing.attr)
print("")
print("Atrybutu przed zmianą")
cos = Cos
print("Cos = "+cos.attr)
print("Thing = "+thing.attr)
cos.attr = "Jestem Cos"
thing.attr = "Jestem Thing"
print("")
print("Atrybuty po zmianie")
print("Cos = "+cos.attr)
print("Thing = "+thing.attr)