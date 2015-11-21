from powerpuzzle import solve

def check(expected, k, start=0):
	actual = solve(k=k, start=start)

	expected[0].sort()
	actual[0].sort()
	expected[1].sort()
	actual[1].sort()
	if expected != actual and expected[0] != actual[1]:
		print('no\nexpected: ' + str(expected) + '\nactual: ' + str(actual))
		print('')
	else:
		print('yay! k=' + str(k) + ', ' + str(actual))

check([[1,2],[0,3]], k=1, start=0)

check([[1, 2, 4, 7],[0, 3, 5, 6]], k=2, start=4)


check([[1, 4, 2, 11, 7, 8, 13, 14], [12, 10, 6, 15, 0, 9, 3, 5]], k=3, start=16)

print(solve(k=4, start=16))

