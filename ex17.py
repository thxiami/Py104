from sys import argv
form os.path import exists

script, from_file, to_file  = argv

print "Copying from %s to %s." % (from_file, to_file)

#we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print "The input_file is %d bytes long." % len(indata)
