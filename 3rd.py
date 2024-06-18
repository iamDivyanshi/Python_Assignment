#Write a python program that calculates the factorial of a given number. 
fact=1
num=int(input("ENTER THE NUMBER : "))
for i in range(2,num+1):
    fact*=i
print("FACTORIAL IS : ",fact)