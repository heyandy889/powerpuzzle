
import math
import random

#For all the numbers 0-n, divide into 2 sets
#whose sums are equal.
#also sums of powers up to k are equal.
def solve(k):
	integers = range(int(math.pow(2,k+1)))
	halfsies = len(integers)/2

	set1 = []
	set2 = []
	while len(set1) < halfsies:
		x = random.choice(integers)
		set1.append(x)
		integers.remove(x)

	while len(set2) < halfsies:
		x = random.choice(integers)
		set2.append(x)
		integers.remove(x)

	return [set1,set2]

