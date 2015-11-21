from powerpuzzle import solve

def check(expected, k):
	actual = solve(k)

	expected[0].sort()
	actual[0].sort()
	expected[1].sort()
	actual[1].sort()
	if expected != actual:
		if expected[0] != actual[1]:
			print('no\n' + str(expected) + '\n' + str(actual))
			print('')

check([[1,2],[0,3]], 1)

check([[1, 2, 4, 7],[0, 3, 5, 6]], 2)


check([[1, 4, 2, 11, 7, 8, 13, 14], [12, 10, 6, 15, 0, 9, 3, 5]], 3)

print(solve(4))

