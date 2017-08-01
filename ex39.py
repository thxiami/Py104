# ex39
ten_things = "Apple Orange iPone iPad iTouch Mac"
stuff = ten_things.split(' ') split(ten_things, ' ')

print("Wait there's not 10 things in that list, let's fix that")

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) < 10:
    next_one = more_stuff.pop() # pop(more_stuff, 0)
    print('Adding:', next_one)
    stuff.append(next_one) # append(stuff, next_one)
    print('There are {} items in the list'.format(len(stuff)))

print stuff[1]
print stuff[-1]
print ' '.join(stuff) # join(' ', stuff)
print '#'.join(stuff[3:5]) # join('#', stuff[3:5])