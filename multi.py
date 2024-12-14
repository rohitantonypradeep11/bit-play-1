def abc(n,number):
    a = 1
    if n&a==1 or n&a==0:
        if number&(1<<(n-1)):
            print("set")
        else:
            print("not set")
n = int(input("enter a number"))
number = int(input("enter another number"))
abc(n,number)