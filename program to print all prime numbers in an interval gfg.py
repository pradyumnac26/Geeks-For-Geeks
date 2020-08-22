start = 11
end = 25
  
for val in range(start, end + 1): 
    if val > 1: 
        for n in range(2, val//2 + 2): 
            if (val % n) == 0: 
                break
            else: 
                if n == val//2 + 1: 
                    print(val) 

////////////
lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
