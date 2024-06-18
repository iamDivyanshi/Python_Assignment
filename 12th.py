#Write a python program that calculates the sum of the digits of a given number
n=int(input("ENTER THE NUMBER : "))
sum=0
while n>0:
    rem=n%10
    sum+=rem
    n//=10
print("ANS IS : ",sum)