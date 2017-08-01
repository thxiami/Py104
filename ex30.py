people = int(raw_input('People ?> '))
cars = int(raw_input('Cars ?> '))
buses = int(raw_input('Buses ?> '))

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can not decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can not decide."

