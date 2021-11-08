import sys
import codecs
file = open('file.txt', 'r')
mydict={}
while True:
    char = file.read(1)
    if char == ' ':
        continue
    if char in mydict.keys():
        mydict[char]=mydict[char]+1
        print('dot')
    else:
        if not char:
            break
        mydict[char]=1
		

print(mydict)

file.close()

data_sorted = {k: v for k, v in sorted(mydict.items(), key=lambda x: x[1])}

print(data_sorted)
newlist=list(reversed(data_sorted))
print(newlist)

frlist=['E','A','T','O','S','N','I','R','H','L','D','U','Y','C','M','W','P','F','B','k','V','X','G','Z','J']
i=0

newdict={}
while(i<len(newlist)):
    newdict[newlist[i]]=frlist[i]
    i=i+1
print(newdict)

file = open('file.txt', 'r')
with open('file2.txt', 'w') as f:
    while True:
        char = file.read(1)
        if char :
            if char == ' ':
                f.write(' ')
            else:
                f.write(newdict[char])
        if not char:
            break
file.close()
f.close()