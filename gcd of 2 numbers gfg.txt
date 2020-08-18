// C++ program to find GCD of two numbers 
#include <iostream> 
using namespace std; 
// Recursive function to return gcd of a and b 
int gcd(int a, int b) 
{ 
	// Everything divides 0 
	if (a == 0) 
	return b; 
	if (b == 0) 
	return a; 

	// base case 
	if (a == b) 
		return a; 

	// a is greater 
	if (a > b) 
		return gcd(a-b, b); 
	return gcd(a, b-a); 
} 

// Driver program to test above function 
int main() 
{ 
	int a = 98, b = 56; 
	cout<<"GCD of "<<a<<" and "<<b<<" is "<<gcd(a, b); 
	return 0; 
} 



efficient aolutin :
/
#include <iostream> 
using namespace std; 
// Recursive function to return gcd of a and b 
int gcd(int a, int b) 
{ 
    if (b == 0) 
        return a; 
    return gcd(b, a % b);  
      
} 
   
// Driver program to test above function 
int main() 
{ 
    int a = 98, b = 56; 
    cout<<"GCD of "<<a<<" and "<<b<<" is "<<gcd(a, b); 
    return 0; 
} 


/////////
# Python program to find LCM of two numbers 

# Recursive function to return gcd of a and b 
def gcd(a,b): 
	if a == 0: 
		return b 
	return gcd(b % a, a) 

# Function to return LCM of two numbers 
def lcm(a,b): 
	return (a*b) / gcd(a,b) 

# Driver program to test above function 
a = 15
b = 20
print('LCM of', a, 'and', b, 'is', lcm(a, b)) 

# This code is contributed by Danish Raza 
