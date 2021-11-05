# You have a non-empty set , and you have to execute N  commands given in N lines.

# The commands will be pop, remove and discard.

# Input Format

# The first line contains integer n , the number of elements in the set s .
# The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9.
# The third line contains integer N, the number of commands.
# The next N lines contains either pop, remove and/or discard commands followed by their associated value.

# Sample Input

# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop 
# discard 6
# remove 5
# pop 
# discard 5

# Sample Output
#   4

# Explanation
#   After completing these 10 operations on the set, we get set([4]). Hence, the sum is 4.
# Note: Convert the elements of set s to integers while you are assigning them. To ensure the proper input of the set, we have added the first two lines of code to the editor.


n = int(input())
s = set(map(int, input().split()))
n1 = int(input())
# Solution 1
# for i in range(n1):
#     cmd = input().split()
#     opr = cmd[0]
#     if opr == 'pop':
#         s.pop()
#     elif opr == 'discard':
#         c1 = int(cmd[1])
#         s.discard(c1)
#     elif opr == 'remove':
#         c1 = int(cmd[1])
#         s.remove(c1)
# print(sum(s))

# Solution 2 - less lines | bit complicated to understand
# for i in range(n1):
    # a, *b =  map(str, input().split()) #a = remove, *b(unpacking) = 9
    # getattr will get the methods of the object
    # s = set, a = operation(pop/remove/discard) => s.remove(<stuff>)
    # <stuff>) => *(int(x) for x in b) is a generator expression => *[0,2]
    # => s.remove(*[0, 2]) [* => argument unpacking]
    # * before a sequence will iterate the sequence and turn its members into function call arguments.
#     getattr(s,a)(*(int(x) for x in b)) # or below
    # getattr(s,attr)(*(map(int, *kw)))

# print(sum(s))

# Solution 3- using eval-> Easy || Clear || Understandable (avoid using eval- bad practice due to security)
# for _ in range(n1): 
#     command = input().split()
#     cmd  = command[0]
#     args = ""
#     if len(command)>1 :
#         args = command[1]        
#     eval("s."+cmd+"("+args+")")
# print(sum(s))

# Solution 4 - Using dictionary - Clean and elegant
oprtn_dict = {'pop':s.pop, 'discard':s.discard,'remove':s.remove}
for _ in range(n1):
    command = input().split()
    oprtn_dict[command[0]](int(command[1])) if len(command) > 1 else oprtn_dict[command[0]]()
print(sum(s))

