#define two Sets

A={1,2,3,4}
B={3,4,5,6}

#set operations in action

union_set=A.union(B) # or A | B
intersection_set=A.intersection(B)
diference_set=A.difference(B) # or A - B
symmetric_difference_set=A.symmetric_difference(B)

# or A ^ B
# or A & B
print("Set A:", A)
print("Set B:", B)

print("Union of A and B:", union_set, )
print("Intersection of A and B:", intersection_set)
print("Difference of A and B:", diference_set)
print("Symmetric Difference of A and B:", symmetric_difference_set)
# Output the results