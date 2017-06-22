r=input("enter the string")
le=len(r)
c=0
for i in r:
	if i.isalpha():
		print("%s is a character"%(i))
		c=c+1
	else:
		print("%s is not a character"%(i))
if c==le:
	print("all are characters")
else:
	print("all are not characters")
