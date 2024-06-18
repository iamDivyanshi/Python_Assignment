#Write a program in python that counts the frequency of each character in a string.
s = "Hii!How are you?"

freq = {}

for i in s:
	if i in freq:
		freq[i] += 1
	else:
		freq[i] = 1

# printing result
print("Count of all characters in GeeksforGeeks is :\n "
	+ str(freq))
