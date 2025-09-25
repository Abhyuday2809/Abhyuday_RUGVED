import math
a=input("Enter a number ")
copy=a
sum=0
a=a[::-1]
for i in range(1,len(a),2):
    k=int(a[i])*2
    if k<10:
        sum+=k
    else:
        sum+= k-9
for i in range(0,len(a),2):
    sum+=int(a[i])
if(sum%10==0):
    print(f"{copy} is a number validated by Luhn's Algorithm ")
else:
   print(f"{copy} is a number not validated by Luhn's Algorithm ")