# s='ok vellidappu cheppandi'
s=input("Enter INput text to be converted to morse: ")

d={'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..'}
D={}
for k,v in d.items():
    if k.isupper():
        D[k.lower()]=d[k]
        D[k]=d[k]
# print(D)



morse=''
for i in s:
    if i==' ':
        morse=morse+'  '
        # print(' ',end='')
    else:
        morse=morse+D[i]+' '
        # print(D[i],end=' ')
print(morse)   

