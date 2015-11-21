
import math
import random
from time import sleep

#For all the numbers 0-n, divide into 2 sets
#whose sums are equal.
#also sums of powers up to k are equal.
def solve(k, start=0):

	while True:
		integers = range(start, int(math.pow(2,k+1)))
		halfsies = int(math.pow(2,k+1)) / 2
		set1 = [1, 4, 2, 11, 7, 8, 13, 14]
		set2 = [12, 10, 6, 15, 0, 9, 3, 5]
		while len(set1) < halfsies:
			x = random.choice(integers)
			set1.append(x)
			integers.remove(x)

		while len(set2) < halfsies:
			x = random.choice(integers)
			set2.append(x)
			integers.remove(x)
		#print[set1,set2]
		exp = k
		things_are_ok = True
		while things_are_ok and exp > 0:
			a = [i**exp for i in set1]
			b = [i**exp for i in set2]
			if sum(a) != sum(b):
				things_are_ok = False
			exp -= 1

		if things_are_ok:
			return [set1, set2]


