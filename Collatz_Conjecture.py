#Set starting number
num = 28

#Initialize iterator
i = 0

#Start main loop
while num != 1:
    print (num)
    if num % 2 == 0:
        num /= 2
    else:
        num = num * 3 + 1
    i += 1
    
print ("It took", i, "steps to reach", num)
