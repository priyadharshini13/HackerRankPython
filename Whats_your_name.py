# https://www.hackerrank.com/challenges/whats-your-name/problem

# Sample Input 0

  # Ross
  # Taylor
# Sample Output 0

# Hello Ross Taylor! You just delved into python.

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    # Solution 1
    # full_name = 'Hello ' + first + ' ' + last + '! You just delved into python.'
    # print(full_name)
    
    # Solution 2
    # print "Hello {0} {1}! You just delved into python.".format(input(), input())
    # print("Hello {input()} {input()}! You just delved into python.")
    print("Hello {0} {1}! You just delved into python.".format(first, last))

    #Solution 3 - python2.7
#     print("Hello %s %s! You just delved into python." %(first, last))

    
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
