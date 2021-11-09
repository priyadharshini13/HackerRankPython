# .difference()
# The tool .difference() returns a set with all the elements from the set that are not in an iterable.
# Sometimes the - operator is used in place of the .difference() tool, but it only operates on the set of elements in set.
# Set is immutable to the .difference() operation (or the - operation).

# Task
# Students of District College have a subscription to English and French newspapers. Some students have subscribed to only the English newspaper,
# some have subscribed to only the French newspaper, and some have subscribed to both newspapers.
# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper.
# Your task is to find the total number of students who have subscribed to only English newspapers.

# Input Format
# The first line contains the number of students who have subscribed to the English newspaper.
# The second line contains the space separated list of student roll numbers who have subscribed to the English newspaper.
# The third line contains the number of students who have subscribed to the French newspaper.
# The fourth line contains the space separated list of student roll numbers who have subscribed to the French newspaper.

# Output Format
# Output the total number of students who are subscribed to the English newspaper only.

# Sample Input
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8

# Sample Output
# 4
# -------------------------------

# Enter your code here. Read input from STDIN. Print output to STDOUT
# Solution 1 - Simple | More Readable
# _, eng = input(), set(input().split())
# _, frn = input(), set(input().split())
# print(len(eng.difference(frn)))

# Solution 2 - One liner | Less readable
# print(len(input()== 0 or set(input().split()).difference(input() == 0 or set(input().split()))))

# Solution 3 - Two lines | Less readable
# size_1,eng,size_2,frn = (set(input().split()) for i in range(4))
# print(len(eng - frn))

eng, frn = map(set, [input().split() for i in range(4)][1::2])
print(len(eng - frn))
