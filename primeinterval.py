low=int(raw_input("enter the 1st no"))
up=int(raw_input("enter the 2nd no"))
for num in range(low+1,up):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
