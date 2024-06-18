#Write a python program that generates the first n numbers in the Fibonacci sequence.
n=int(input("ENTER THE NUMBER : "))
a=0
b=1
if n<=1:
    print("0")
elif n==2:
    print("0,1")
else:
    for i in range(0,n-2):
        if i==0:
            print("0 ,")
        print(b,",")
        c=a+b
        a=b
        b=c
    print(b)
        