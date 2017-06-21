num=int(input("enter the number"))
f=0
for a in range(2, num):
    if num % a== 0:
        f=1
        break
if(f==0):
    print("prime")
else:
	print("not prime")
