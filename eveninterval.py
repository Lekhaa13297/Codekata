f=int(raw_input("enter the 1st no"))
f1=int(raw_input("enter the 2nd no"))
l=[]
for i in range(f+1,f1):
    if i%2==0:
        l.append(i)
print(l)
