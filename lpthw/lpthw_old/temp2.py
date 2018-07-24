seven_things = 'sword, ring, bow, armor, crossbow'

print seven_things

stuff = seven_things.split(', ')
print stuff

next_list = ['spoon', 'bottle']

while len(stuff) !=7:
	next = next_list.pop()
	stuff.append(next)
	
print stuff
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # super stellar!