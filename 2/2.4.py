# chapter 2.4
# Subject: zagneżdżone if
# Time: 8 minutes
# GO!

print('welcone in millioners')

key = input('imput number 1-3: ')

if key=='1':
    print("private customer help")
    key = input('imput number 1-3: ')
    if key=='1':
        print('wifi help')
    elif key=='2':
        print('phone help')
        key = input('imput number 1-3: ')
        if key == '1':
            print('change phone number')
        elif key =='2':
            print('mobile internet information')
        elif key =='3':
            print('exit')
    elif key == '3':
        print('exit')
elif key=="2":
    print("firm customer help")
elif key=="3":
    print("exit")
else:
    print("niezgodny wybór")

    

