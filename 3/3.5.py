# chapter 3.5
# Subject: multiple arrays
# Time: 5 minutes
# GO!

from array import array
aaa = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]
print(aaa)

for x in range(0, len(aaa)):
    print(aaa[x])
print("2x loop #1")
for i in range(0, len(aaa)):
    for j in range(0, len(aaa[i])):
        print(aaa[i][j])

print("2x loop #2")
out =""
for i in range(0, len(aaa)):
    for j in range(0, len(aaa[i])):
        out+= str(aaa[i][j])+"; "
        if j==len(aaa[i])-1:
            out+='\r\n'
print(out)


