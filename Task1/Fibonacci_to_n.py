# fibonacci is= 0,1,1,2,3,5,8,13,21......n
n=int(input("Enter the limit"))
a=0
b=1
for i in range(0,n):
    print(a,end=" ")
    temp=a
    a=b
    b+=temp
   