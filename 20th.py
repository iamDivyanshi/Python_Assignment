#Write a python program that takes a list of numbers and returns their sum.
list=[1,2,3,4,5]
sum=0
for i in range(0,len(list)):
    sum+=list[i]
print("SUM IS : ",sum)