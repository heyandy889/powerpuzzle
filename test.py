from powerpuzzle import solve

def check(expected, k):
	actual = solve(k)

	expected[0].sort()
	actual[0].sort()
	expected[1].sort()
	actual[1].sort()
	assert expected == actual, '\n' + str(expected) + '\n' + str(actual)

check([[1,2],[0,3]], 1)

check([[1, 2, 4, 7],[0, 3, 5, 6]], 2)


