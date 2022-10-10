# Write a Python program to write a list to a file. 


names = ['Raj', 'deep', 'tom']

# open file in write mode
with open(r'--', 'w') as fp:
    for item in names:
        # write each item on a new line
        fp.write("%s\n" % item)
    print('Done')