# Write a python program that counts the occurrences of a specific element in a list
l=[2,2,4,5,8,2]
n=int(input("ENTER THE NUMBER TO CHECK FOR OCCURENCES : "))
cnt=0
for i in range(0,len(l)):
    if l[i]==n:
        cnt+=1
print("COUNT OF",n,"is : ",cnt)