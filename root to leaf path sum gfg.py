def hasPathSum(root, sm):
    '''
    :param root: root of given tree.
    :param sm: root to leaf sum
    :return: true or false
    '''
    if root is None: 
        return False
  
    else: 
        ans = 0 
          
        # Otherwise check both subtrees 
        subSum = sm - root.data  
          
        # If we reach a leaf node and sum becomes 0, then  
        # return True  
        if(subSum == 0 and root.left == None and root.right == None): 
            return True 
  
        if root.left is not None: 
            ans = ans or hasPathSum(root.left, subSum) 
        if root.right is not None: 
            ans = ans or hasPathSum(root.right, subSum) 
  
        return ans  
