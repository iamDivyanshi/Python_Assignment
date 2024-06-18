#Write a python program that checks whether a given number is even or odd
num=int(input("ENTER THE NUMBER : "))
if num<0 :
    print(num," is NEGATIVE")
elif num==0 :
    print(num," is ZERO")
elif num%2==0 : 
    print(num," is EVEN")
else :
    print(num," is ODD")