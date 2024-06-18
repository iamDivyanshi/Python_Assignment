# Write a python program that checks if two strings are anagrams of each other.
s1=input("ENTER 1st STRING : ")
s2=input("ENTER 2nd STRING : ")
str1=s1.lower()
str2=s2.lower()
if sorted(str1) == sorted(str2):
    print("YES THEY ARE ANAGRAMS!!")
else:
    print("NO,THEY ARE NOT ANAGRAMS!!")
