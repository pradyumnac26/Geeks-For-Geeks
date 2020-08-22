# Find the minimum product among all combinations of triplets in the list
def minimumProductTriplet(A):

	n = len(A)
	if n <= 2:
		return float('inf')

	# Sort the given list in natural order
	A.sort()

	# Consider minimum of first three elements or
	# first element and last two elements
	return min(A[n-1] * A[n-2] * A[0], A[0] * A[1] * A[2])


if __name__ == '__main__':

	A = [4, -1, 3, 5, 9]

	min = minimumProductTriplet(A)

	if min == float('inf'):
		print("No triplet exists since the list has less than 3 elements")
	else:
		print("The minimum product is", min)
