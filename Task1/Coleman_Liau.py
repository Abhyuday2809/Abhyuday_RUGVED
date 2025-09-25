sen=input("Enter a string")
sentences=0
words=len(sen.split(' '))
length= len(sen)
for a in sen:
    if a=='.' or a=='!' or a=='?':
        sentences+=1
l = (length / words) * 100
s= (sentences / words) * 100
coleman=0.588*l-0.296*s-15.8

print(f'The Coleman-Liau index for the srting "{sen}" is =  {coleman}')


