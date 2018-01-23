import helloworld

f = open('output.txt', 'w')
output = helloworld.out
print output()
print type(output())
f.write(output())
f.close()

print "its nice"
