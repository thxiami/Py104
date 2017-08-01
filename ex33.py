i = 0
numbers = []
while i < 6:
    print"="*20
    print "At the top i is {}".format(i)
    numbers.append(i)
    
    i += 1
    print "numbers: ", numbers
    print "At the bottom i is %d" % i

for num in numbers:
    print "num:", num

# addtional exercise
def while_loop(count):
    i = 0
    numbers = []
    while i < count:
        print"="*20
        print "At the top i is {}".format(i)
        numbers.append(i)

        i += 1
        print "numbers: ", numbers
        print "At the bottom i is %d" % i

    for num in numbers:
        print "num:", num

# run the function
while_loop(6)