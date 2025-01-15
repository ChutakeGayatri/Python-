a=int(input("Enter First No:"))
b=int(input("Enter Second No:"))
c=int(input("Enter Third No:"))
if(a>b) & (a>c):
    print(a,"is Greatest")
elif(b>a) & (b>c):
    print(b,"is Greatest")
else:
    print(c,"is Greatest")
