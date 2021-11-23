# chapter 2.6
# Subject: zagneżdżone if
# Time: 8 minutes
# GO!

public = True
close = False
form = None
if public == True and close!=False and form!=None:
    print("formulaż rejestracji")
else:
    if form == None:
        print("brak formulaży") 
    if close == True:
        print("Rejestracja zamknieta")
    if public == False:
        print("Formulaz niepubliczny")