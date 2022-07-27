#Write a Python function to reverses a string if its length is a multiple of 4.

def reverse(s):
	str = ""
	for i in s:
		str = i + str
	return str

s = "ghost"

print("The string is : ", end="")
print(s)

print("The reversed string is : ", end="")
print(reverse(s))
