# .symmetric_difference()
# The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both.
# Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set of elements in set.
# The set is immutable to the .symmetric_difference() operation (or ^ operation).


# Task
# Students of District College have subscriptions to English and French newspapers. Some students have subscribed to English only,
# some have subscribed to French only,and some have subscribed to both newspapers.
# You are given two sets of student roll numbers. One set has subscribed to the English newspaper,
# and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to either the 
# English or the French newspaper but not both.

# Input Format

# The first line contains the number of students who have subscribed to the English newspaper.
# The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
# The third line contains the number of students who have subscribed to the French newspaper.
# The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

# Output Format
#   Output total number of students who have subscriptions to the English or the French newspaper but not both.

# Sample Input

# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
# Sample Output

# 8
# Explanation

# The roll numbers of students who have subscriptions to English or French newspapers but not both are:



# Enter your code here. Read input from STDIN. Print output to STDOUT
# # Solution 1 - Direct | More readable | Simple
# _, a = input(), set(input().split())
# _, b = input(), set(input().split())
# print(len(a.symmetric_difference(b)))

#solution 2 - One line - ignoring size input
# print(len(input()==0 or set(input().split()).symmetric_difference(input()==0 or input().split() )))

# Solution 3 - Using ^ operator
# _, a = input(), set(input().split())
# _, b = input(), set(input().split())
# print(len(a ^ b))

# Solution 4 - Without using symmetrical_difference method 
# print(len((a.difference(b)).union(b.difference(a))))

# Solution 5 - Using eval
_,a,_,b = eval("set(input().split()),"*4)
print(len(a ^ b))


