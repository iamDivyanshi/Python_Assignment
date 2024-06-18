# Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
s=input("ENTER THE STRING : ")
prefix=input("ENTER THE STRING(for prefix) : ")
suffix=input("ENTER THE STRING(for suffix) : ")
if s.startswith(prefix)==1:
    print(s,"starts with",prefix)
else:
    print(s,"does not starts with",prefix)
if s.endswith(suffix)==1:
    print(s,"ends with",suffix)
else:
    print(s,"does not ends with",suffix)