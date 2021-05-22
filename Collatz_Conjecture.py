#Get starting number from user
num = -1
while num <= 0:
	user_response = input ("Enter a positive integer to start with? ")
	num = int(user_response)

#Initialize iterator
i = 0

#Print the starting number
print ("Testing new vimrc with Python code")
print ("Starting number =", num)

#Start main loop
while num != 1:
    i += 1
    if num % 2 == 0:
        num /= 2
    else:
        num = num * 3 + 1
    print (num)
    
print ("It took", i, "steps to reach", num)
