# https://www.hackerrank.com/challenges/no-idea/problem
# There is an array of  integers. There are also  disjoint sets,  and , each containing integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is . For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.
# Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.

# Input Format

# The first line contains integers  and  separated by a space.
# The second line contains  integers, the elements of the array.
# The third and fourth lines contain  integers,  and , respectively.

# Output Format

# 	Output a single integer, your total happiness.

# Sample Input
  # 3 2
  # 1 5 3
  # 3 1
  # 5 7
# Sample Output
  # 1
# Explanation

# You gain  unit of happiness for elements  and  in set . You lose  unit for  in set . The element  in set  does not exist in the array so it is not included in the calculation.
# Hence, the total happiness is 1.



# Enter your code here. Read input from STDIN. Print output to STDOUT

# Solution 1 - wrong
# 1. convert array to set
# 2. r1 = take intersection of set_array and set_a
# 3. r2 take Intersection of set_array and set_b
# 4. len of r1 - len of r2 => total happiness
# array_to_set = set(array)
# intersection_a = array_to_set.intersection(likes)
# intersection_b = array_to_set.intersection(dislikes)
# print(abs(len(intersection_a) - len(intersection_b)))

# Solution 2 - right
# _ = input()
# array = input().split()
# likes = set(input().split())
# dislikes = set(input().split())
# print(sum((i in likes) - (i in dislikes) for i in array))

# Solution 3
n,m = map(int,input().split())
N = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
#Union set A & B
C = A | B
#Exclude all numbers which doesn't exit in both A & B
N = (i for i in N if i in C)
#Add 1 if number is in set A else subtract 1
print(sum(1 if i in A else -1 for i in N ))
