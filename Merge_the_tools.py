# Complete the merge_the_tools function in the editor below.
# merge_the_tools has the following parameters:
    # string s: the string to analyze
    # int k: the size of substrings to analyze
# Prints
    # Print each subsequence on a new line. There will be n/k of them. No return value is expected.

# Input Format
    # The first line contains a single string, s.
    # The second line contains an integer, k, the length of each substring.

# Sample Input
    # STDIN       Function
    # -----       --------
    # AABCAAADA   s = 'AABCAAADA'
    # 3           k = 3

# Sample Output
    # AB
    # CA
    # AD
import re
def merge_the_tools(string, k):
    # length of string
    len_str = len(string)

    # splitting the string into 'k' length
    parts = [string[i:i+k] for i in range(0, len_str, k)]
    
    for i in range(len(parts)):
        distinct = set(parts[i])
        # Solution 1 - if order doesn't matter
        # print(''.join(distinct))
        
        # Solution 2 - if order doesn't matter
        print(''.join(sorted(distinct, key=parts[i].index)))
        
        # Solution 3 - Using dictionary - fromkeys preserves insertion order
        # print(''.join(dict.fromkeys(parts[i])))
        
        #Solution 4 - Using regex - below not right
        
        # pattern = r'(.)\1+' #(.)any character, \+ - repeated more than
        # replace = r'\1' #replace once with nothing
        # element = parts[i]
        # print(re.sub(pattern,replace, element))
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
