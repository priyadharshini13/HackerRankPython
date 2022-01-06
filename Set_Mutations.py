# TASK
# You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.
# Your task is to execute those operations and print the sum of elements from set .

# Input Format

# The first line contains the number of elements in set .
# The second line contains the space separated list of elements in set .
# The third line contains integer , the number of other sets.
# The next  lines are divided into  parts containing two lines each.
# The first line of each part contains the space separated entries of the operation name and the length of the other set.
# The second line of each part contains space separated list of elements in the other set.

#  len(set(A)) 
#  len(otherSets) 

# Output
# Output the sum of elements in set .

# Sample Input

#  16
#  1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
#  4
#  intersection_update 10
#  2 3 5 6 8 9 1 4 7 11
#  update 2
#  55 66
#  symmetric_difference_update 5
#  22 7 35 62 58
#  difference_update 7
#  11 22 35 55 58 62 66

# Sample Output
# 38


# 1. Read size of the set
size_setA = int(input())
# 2. Read set elements
setA = set(map(int, input().split()))
# 3. Read number of operations
no_of_operations = int(input())
for i in range(no_of_operations):
    opr = input().split()
    elements = set(map(int, input().split()))
    
    if(opr[0] == 'intersection_update'):
        setA.intersection_update(elements)
    elif(opr[0] == 'update'):
        # update operation 
        setA.update(elements)
    elif(opr[0] == 'difference_update'):
        # difference_update 
        setA.difference_update(elements)
    elif(opr[0] == 'symmetric_difference_update'):
        # symmetric_difference_update 
        setA.symmetric_difference_update(elements)

print(sum(setA))
