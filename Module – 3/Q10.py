# Write a Python program to check whether a list contains a sub list 

test_list = [5, 6, 3, 8, 2, 1, 7, 1]

print("The original list : " + str(test_list))

sublist = [8, 2, 1]

res = False
for idx in range(len(test_list) - len(sublist) + 1):
		if test_list[idx : idx + len(sublist)] == sublist:
			res = True
			break
		
print("Is sublist present in list ? : " + str(res))
