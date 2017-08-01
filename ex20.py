from sys import argv
script, input_file = argv

def print_all(file):
    print file.read()
    
def rewind(file):
    file.seek(0)
    
def print_line(line, file):
    print line, file.readline(),
    
print "Let's print the whole file first.\n"
current_file = open(input_file)
print_all(current_file)

print "Let's rewind the file.\n"
rewind(current_file)

print "Let's print three lines: "
current_line = 1
print_line(current_line, current_file)

current_line += 1
print_line(current_line, current_file)

current_line += 1
print_line(current_line, current_file)