# Python3 program to
# count trailing 0s
# in n!

# Function to return
# trailing 0s in
# factorial of n


def findTrailingZeros(n):

	# Initialize result
	count = 0

	# Keep dividing n by
	# 5 & update Count
	while(n >= 5):
		n //= 5
		count += n

	return count


# Driver program
n = 100
print("Count of trailing 0s " +
	"in 100! is", findTrailingZeros(n))

# This code is contributed by Uttam Singh
