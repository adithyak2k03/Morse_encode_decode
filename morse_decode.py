s='this is a secret message'

d={'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..'}
D={}
for k,v in d.items():
    if k.isupper():
        D[k.lower()]=d[k]
        D[k]=d[k]
        
morse=''
for i in s:
    if i==' ':
        morse=morse+'  '
        # print(' ',end='')
    else:
        morse=morse+D[i]+' '
        # print(D[i],end=' ')
# print(morse)    
# print(morse)

# morse='--- -.-   ...- . .-.. .-.. .. -.. .- .--. .--. ..-   -.-. .... . .--. .--. .- -. -.. .. '
morse=input("Enter the morse code here to be decoded: ")
newmorse=[]
l=morse.split('  ')
for i in range(len(l)):
    newmorse.append(l[i].split())
# print(newmorse)

d2={}
for i in D.keys():
    d2[D[i]]=i.lower()
# print(d2)


for i in range(len(newmorse)):
    for j in range(len(newmorse[i])):
        print(d2[newmorse[i][j]],end='')
    print(' ',end='')
        # print(newmorse[i][j])
