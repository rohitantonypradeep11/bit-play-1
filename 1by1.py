def abs(n):
    once = 0
    zero = 0
    while(n):
        if n&1==1:
            once = once+1
        else:
            zero = zero + 1
        n>>=1
    print(once,zero)
number = int(input("enter a number"))
abs(number)