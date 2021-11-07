# .union()

# The .union() operator returns the union of a set and the set of elements in an iterable.
# Sometimes, the | operator is used in place of .union() operator, but it operates only on the set of elements in set.
# Set is immutable to the .union() operation (or | operation).

# Example

# >>> s = set("Hacker")
# >>> print s.union("Rank")
# set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])


# Task
#   The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, 
#   some have subscribed to only French and some have subscribed to both newspapers.
#   You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. 
#   The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.

# Input Format
#   The first line contains an integer,n , the number of students who have subscribed to the English newspaper.
#   The second line contains n space separated roll numbers of those students.
#   The third line contains b, the number of students who have subscribed to the French newspaper.
#   The fourth line contains b space separated roll numbers of those students.

# Output Format
#   Output the total number of students who have at least one subscription.

# Sample Input

# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8

# Sample Output
# 13
# -----------------------------------------
# Enter your code here. Read input from STDIN. Print output to STDOUT
  # SOLUTION 1 - Readable | Simple
# english_sub = int(input())
# eng_sub_list = set(map(int,input().split()))
# french_sub = int(input())
# fre_sub_list = set(map(int, input().split()))
# full_stdnts = eng_sub_list.union(fre_sub_list)
# print(len(full_stdnts))

  # Solution 2 - three lines | Less readable
# input().split() => need not map the result list to int
# eng_size, eng_subscrptn = input(), input().split()
# frnch_size, frnch_subscrptn = input(), input().split()
# print(len(set(eng_subscrptn).union(set(frnch_subscrptn))))

  # Solution 3 - three lines | More readable
# eng_size, eng_subscrptn = input(), set(input().split())
# frnch_size, frnch_subscrptn = input(), set(input().split())
# # print(len(eng_subscrptn.union(frnch_subscrptn)))
    # # Using '|' operator
# print(len(eng_subscrptn |frnch_subscrptn))

  # Solution 4 - two lines | Less readability
    # [1::2] => list[start:stop:step]
    # for x in range(4) => 4 lines of input
    # input().split() for x in range(4) => result => [['9'],[1,2,3,4,5, 6, 7, 8, 9],['9']       ,[10,1,2,3,11,21,55,6,8]]
        # b, a = result[1::2] => 0th element -> ['9']
        # b= 1st element -> [1,2,3,4,5, 6, 7, 8, 9], 2nd element -> ['9']
        # a ->3rd element(step = 2, so 3rd element of l) -> [10,1,2,3,11,21,55,6,8]
        # map(set, [],[]) => converts each list to set and assigns it to b, a
# b,a = map(set,[input().split() for x in range(4)][1::2])
# print(len((b).union(a)))
 
  # Solution 5 - one line | very less readable
    # input() == 0 is always evaluated to False(it has to!), so we consume one line of input and go ahead for processing second part of 'or'.
print(input() == 0 or len(set(input().split()).union(input() == 0 or input().split())))

