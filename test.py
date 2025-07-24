#sum of n natural numbers using recursion and formula
# Formula: n(n+1)/2
# Recursive function to calculate sum of first n natural numbers
def sum_n(n):
    #"""Returns the sum of the first n natural numbers using recursion."""
     if n==0:
          return 0
     else:
          return n + sum_n(n-1)
for  i in range(1,11):
     recursive=sum_n(i)
     formula_sum=i *(i+1)//2
     print(f"n={i}: Recursive Sum={recursive},Formula Sum={formula_sum}")