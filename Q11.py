#13. Write a Python program to count the number of characters (character frequency) in a string


test_str = "this is python"
  
# using naive method to get count 
# of each element in string 
all_freq = {}
  
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
  
# printing result 
print ("Count of all characters in this is python is :\n "
                                        +  str(all_freq))