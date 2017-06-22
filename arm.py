r=int(input("enter the number"))
q=r
pr=0
le=len(str(r))
while q!=0:
	n=q%10
	pr+=n**le
	q=q//10
if (int(r)==pr):
	print("armstrong")
else:
	print("not armstrong")
		
