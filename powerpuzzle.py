
import math
import random

#For all the numbers 0-n, divide into 2 sets
#whose sums are equal.
#also sums of powers up to k are equal.
def solve(k):

	while True:
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

		exp = 1
		things_are_ok = True
		while things_are_ok and exp < k+1:
			a = [i**exp for i in set1]
			b = [i**exp for i in set2]
			if sum(a) != sum(b):
				things_are_ok = False
				if(exp > 3):
					print exp
					print set1
					print set2
			exp += 1

		if things_are_ok:
			return [set1, set2]


