////////Brute force method 

def maxLen(n, arr):
    max_len = 0
  
    # pick a starting point 
    for i in range(len(arr)): 
          
        # initialize sum for every starting point 
        curr_sum = 0
          
        # try all subarrays starting with 'i' 
        for j in range(i, len(arr)): 
          
            curr_sum += arr[j] 
  
            # if curr_sum becomes 0, then update max_len 
            if curr_sum == 0: 
                max_len = max(max_len, j-i + 1) 
  
    return max_len 

////////////////
hashing 

def maxLen(arr): 
      
    # NOTE: Dictonary in python in implemented as Hash Maps 
    # Create an empty hash map (dictionary) 
    hash_map = {} 
  
    # Initialize result 
    max_len = 0
  
    # Initialize sum of elements 
    curr_sum = 0
  
    # Traverse through the given array 
    for i in range(len(arr)): 
          
        # Add the current element to the sum 
        curr_sum += arr[i] 
  
        if arr[i] is 0 and max_len is 0: 
            max_len = 1
  
        if curr_sum is 0: 
            max_len = i + 1
  
        # NOTE: 'in' operation in dictionary to search  
        # key takes O(1). Look if current sum is seen  
        # before 
        if curr_sum in hash_map: 
            max_len = max(max_len, i - hash_map[curr_sum] ) 
        else: 
  
            # else put this sum in dictionary 
            hash_map[curr_sum] = i 
  
    return max_len 
