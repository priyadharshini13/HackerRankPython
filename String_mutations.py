# https://www.hackerrank.com/challenges/python-mutations/problem
# Sample Input
# STDIN           Function
# -----           --------
# abracadabra     s = 'abracadabra'
# 5 k             position = 5, character = 'k'

# Sample Output
#   abrackdabra
def mutate_string(string, position, character):
    
    # Solution 1
    # mutated_string = string[:position] + character + string[position+1:]
    # return mutated_string
    
    # Solution 2
    # convert string to list as string is immutable
    # list_string = list(string)
    # list_string[position] = character
    # mutated_string = ''.join(list_string)
    # return mutated_string

    # Solution 3
    return ("{}{}{}".format(string[:position], character, string[position+1:]))

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
