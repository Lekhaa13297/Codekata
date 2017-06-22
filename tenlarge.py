l=[]
for i in range(10):
	r1=int(input("enter the %s number"%(i)))
	l.append(r1)
l.sort()
print(l)
print("%s is the largest"%(l[len(l)-1]))
