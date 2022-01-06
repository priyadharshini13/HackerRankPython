# You are given two sets, A and B.
# Your job is to find whether set  is a subset of set .

# If set A is subset of set B, print True.
# If set A is not a subset of set B, print False.

# Sample Input

# 3
# 5
# 1 2 3 5 6
# 9
# 9 8 5 6 3 2 1 4 7
# 1
# 2
# 5
# 3 6 5 4 1
# 7
# 1 2 3 5 6 8 9
# 3
# 9 8 2

# Sample Output

# True 
# False
# False

# Solution
total_testcase = int(input())
for i in range(total_testcase):
    size_setA, setA = int(input()), set(map(int, input().split()))
    size_setB, setB = int(input()), set(map(int, input().split()))
    # Solution 1
    # if setA.issubset(setB):
    #     print('True')
    # else:
    #     print('False')
    
    # Solution 2
    print('True') if setA.issubset(setB) else print('False')
