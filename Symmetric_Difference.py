# Given  sets of integers, M and N , print their symmetric difference in ascending order. 
# The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

# Sample Input
#  STDIN       Function
# -----       --------
  # 4           set a size M = 4
  # 2 4 5 9     a = {2, 4, 5, 9}
  # 4           set b size N = 4
  # 2 4 11 12   b = {2, 4, 11, 12}

# Sample output
  # 5
  # 9
  # 11
  # 12
  
  
  # 1. Read input line 1 - size of set
# 2. Read the space separated values using split - ['2', '4', '5', '9']
# 3. Convert the strings in list to integer by using map [2, 4, 5, 9]
# 4. Convert list to set - set(list(map(int, lst_a)))
# 5. Take the difference
# 6. convert that set result to list and add the 2 symmetric differnce list
# 7. print the result using separator in the print statement

# Solution 1
# set_size_a = input()
# set_a = input()
# list_a = set_a.split()
# int_list_a = set(list(map(int, list_a)))
# set_size_b = input()
# set_b = input()
# list_b = set_b.split()
# int_list_b = set(list(map(int, list_b)))
# #Symmetric difference
# a_minus_b = int_list_a.difference(int_list_b)
# b_minus_a = int_list_b.difference(int_list_a)
# result_list = list(a_minus_b) + list(b_minus_a)
# s_r = sorted(result_list)
# print(*s_r,sep='\n')

# Solution 2
    # 1. Read input
# size_a = input()
# list_a = input().split()
# size_b = input()
# list_b = input().split()
#     # 2. Convert to set
# set_a = set(list(map(int, list_a)))
# set_b = set(list(map(int, list_b)))
#     # 3. Compute the difference
# a_minus_b = int_list_a.difference(int_list_b)
# b_minus_a = int_list_b.difference(int_list_a)
# result_list = list(a_minus_b) + list(b_minus_a)
# s_r = sorted(result_list)
# print(*s_r,sep='\n')

# Solution 3
# M,m=input(),set(list(map(int,input().split())))
# N,n=input(),set(list(map(int,input().split())))
# s = sorted(list(m.difference(n))+list(n.difference(m)))
    # * unpacks the list. Treats each element of the list separately
# print(*s,sep='\n')
# for i in s:
#     print (i)

# Solution 4
    # list[1::2]
    # This means [start:stop:step], like we start at list[1], stop at list[None] (this   means we don't stop till the end of the list) and the step of the exploration is 2, so we got list[1], list[3], etc.
    # In our case, the list has length 4, so by list[1::2]
    # we got members 2 and 4. Finally, with:
    # a,b = [set(raw_input().split()) for _ in range(4)][1::2]
    # the 2 lines are stored in variables a and b.
# a, b = [set(input().split()) for _ in range(4)][1::2]
# print('\n'.join(sorted(a^b, key=int)))

# Solution 5 
_ , M = input(), set(map(int,input().split()))
_ , N = input(), set(map(int,input().split()))
print(*sorted(list(M.symmetric_difference(N))),sep='\n')
