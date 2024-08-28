a=int(input("enter the number"))
b=int(input("enter the number"))
ch=0
while ch<6:
    print("calculator menu")
    print('1.add')
    print('2.sub')
    print('3.multi')
    print('4.division')
    print('5.square')
    print('6.exit')
    ch=int(input("enter ur choice"))
    if ch==1:
        a=a+b
        print(a)
    elif ch==2:
        s=a-b
        print(s)
    elif ch==3:
        m=a*b
        print(m)
    elif ch==4:
        d=a/b
        print(d)
    elif ch==5:
        sq=a**b
        print(sq)
    elif ch==6:
        break
    else:
        print("invalid")
