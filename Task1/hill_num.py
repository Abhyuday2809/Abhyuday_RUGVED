#WAP to check if a number is hill no or not
# No is first increasing and then decreasing strictly

num=input("enter a number")
low_ind=0
#j=len(num)
flag=1
for i in range (0,len(num)-1,1): # getting index of largest number
    if num[i]<=num[i+1]:
        low_ind=i
    else:
        break
for i in range (low_ind+1,len(num)-1,1): # checking for monotonicity
    if num[i]<num[i+1]:
        flag=0
        break
if flag!=0:
    print(f'{num} is a hill number')
else:
    print(f'{num} is not a hill number')