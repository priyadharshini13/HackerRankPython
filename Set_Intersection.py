# .intersection()
# The .intersection() operator returns the intersection of a set and the set of elements in an iterable.
# Sometimes, the & operator is used in place of the .intersection() operator, but it only operates on the set of elements in set.
# The set is immutable to the .intersection() operation (or & operation).

# Task
# The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English
# , some have subscribed only to French, and some have subscribed to both newspapers.

# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, 
# one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.

# Input Format
  # The first line contains , the number of students who have subscribed to the English newspaper.
  # The second line contains  space separated roll numbers of those students.
  # The third line contains , the number of students who have subscribed to the French newspaper.
  # The fourth line contains  space separated roll numbers of those students.

# Output Format
  # Output the total number of students who have subscriptions to both English and French newspapers.

# Sample Input
  # 9
  # 1 2 3 4 5 6 7 8 9
  # 9
  # 10 1 2 3 11 21 55 6 8
  
# Sample Output
  # 5

# --------------

# Enter your code here. Read input from STDIN. Print output to STDOUT
# Solution 1 - 3 line | More readability
# _, a = input(), set(input().split())
# _, b = input(), set(input().split())
# print(len(a.intersection(b)))

# Solution 2 - 2 lines| Less readability
# eng, french = map(set, [input().split() for i in range(4)][1::2])
# print(len(eng.intersection(french)))

# Solution 3 - one line| Very Less readability
print(len(input() == 0 or set(input().split()).intersection(input()== 0 or set(input().split()))))
