# chapter 3.1
# Subject: arrays
# Time: 5 minutes
# GO!

from array import array
a1 = [5,10,15]
a2 = array('i', [5,10,15])
a3 = array('u', ['A', 'B', 'C'])
a4 = [13,'6', True]

# Display

print("display")
print(a2[0])
print(a4[0])
a1.append('abc')
print(a1[3])
a1[1] = 'cba'
print(a1[1])

# Lenght

print('\n Lenght')
print('A1= '+str(len(a1)))
print('A2= '+str(len(a2)))
print('A3= '+str(len(a3)))
print('A4= '+str(len(a4)))