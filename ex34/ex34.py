#!/usr/bin/env python
animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
end = ['st', 'nd', 'rd', 'th']
for i in range(0,6):
	print "The animal at %d is the %d%s animal and is a %s." % (i, i+1,end[i%10 if i%10<3 else 3], animals[i])
