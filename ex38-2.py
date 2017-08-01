# ex38
# creat a mapping state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has:", cities['NY']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']

# do it by using the state and then cities dict
print '-' * 10
print 'Michigan has:', cities[states['Michigan']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print('{} is abbreviated {}'.format(state, abbrev))
    
# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print('{} has the city: {}'.format(abbrev, city))
    
# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print('{} is abbreviated {}'.format(state, abbrev))
    print('{} has the city: {}'.format(abbrev, cities[abbrev]))
    
# safely get a abbreviation by state that might not be there
print '-' * 10
state = states.get('Texas', None)

if state is None:
    print('Sorry, No Texas')
    
# get a city with a default value
print '-' * 10
city = cities.get('TX', 'Does Not Exist.')
print("The city for the state 'TX' is:", city)