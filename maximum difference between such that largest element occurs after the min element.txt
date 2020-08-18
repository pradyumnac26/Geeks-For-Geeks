# Python 3 code to find Maximum difference 
# between two elements such that larger 
# element appears after the smaller number 

# The function assumes that there are 
# at least two elements in array. 
# The function returns a negative 
# value if the array is sorted in 
# decreasing order. Returns 0 if 
# elements are equal 
def maxDiff(arr, arr_size): 
	max_diff = arr[1] - arr[0] 
	min_element = arr[0] 
	
	for i in range( 1, arr_size ): 
		if (arr[i] - min_element > max_diff): 
			max_diff = arr[i] - min_element 
	
		if (arr[i] < min_element): 
			min_element = arr[i] 
	return max_diff 
	
# Driver program to test above function 
arr = [1, 2, 6, 80, 100] 
size = len(arr) 
print ("Maximum difference is", 
		maxDiff(arr, size)) 

# This code is contributed by Swetank Modi 
