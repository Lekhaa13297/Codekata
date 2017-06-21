r=int(raw_input("enter the year"))
a=len(str(r))
if a==4:
    if r%4==0:
        print("It is a leap year")
    else:
        print("it is a non-leap year")
else:
    print("wrong input")
