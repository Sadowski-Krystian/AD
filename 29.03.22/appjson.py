import json
import copy

jsonStr = '{"course": "ad", "unit": "3PT4", "lesson": "20", "dataAt": "2022-03-29", "topic": "Serializacja i deserializacja"}'
print("Ciąg string z danymi JSON")
print(jsonStr)
print("")
print("Strink z danymi Json zadekodwany do  ..")
pyObj = json.loads(jsonStr)
print(pyObj)
print("")
print("klucz=wartość")
print("kurs: "+pyObj['course'])
print("klasa: "+pyObj['unit'])
print("lekcja: "+pyObj['lesson'])
print("Data: "+pyObj['dataAt'])
print("Temat: "+pyObj['topic'])
print("")
print("Zduplicowanie słownika {dict}")
lsn = copy.deepcopy(pyObj)
lsn['unit'] = "3pt5"
lsn['lesson'] = "34"
lsn['dataAt'] = "2022-04-04"
print(lsn)
print(pyObj)
print("")
print("Zakodowanie obiektu Python do stringa ")
jsonStr2 = json.dumps(lsn)
print(jsonStr2)