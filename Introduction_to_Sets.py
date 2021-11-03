# A set is an unordered collection of elements without duplicate entries.
# When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.
# Basically, sets are used for membership testing and eliminating duplicate entries.

# Now, let's use our knowledge of sets and help Mickey.

# Ms. Gabriel Williams is a botany professor at District College. One day,
# she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

# Function Description

# Complete the average function in the editor below.

# average has the following parameters:
#   int arr: an array of integers
    
# Returns
#   float: the resulting float value rounded to 3 places after the decimal
    
# Input Format
#   The first line contains the integer, , the size of .
#   The second line contains the  space-separated integers, .

# Constraints
#   0 < N <= 100

# Sample Input

# STDIN                                       Function
# -----                                       --------
# 10                                          arr[] size N = 10
# 161 182 161 154 176 170 167 171 170 174     arr = [161, 181, ..., 174]

# Sample Output
#   169.375

# Explanation
#   Here, set is the set containing the distinct heights. Using the sum() and len() functions, we can compute the average.


def average(array):
    # 1. convert the list to set
    # 2. Divide sum of set by length of set
    # 3. Return the result 
    # Solution 1
    # list_to_set = set(array)
    # avg = float(sum(list_to_set) / len(list_to_set))
    # return avg
    
    # Solution 2 - 2 lines but set conversion needed just once
    # list_to_set = set(array)
    # return float(sum(list_to_set) / len(list_to_set))
    
    # Solution 3 - one line but need to convert to set twice - Less readable
    # return float(sum(set(array)) / len(set(array)))
    
    # Solution 4 - one liner with string format.Need to convert to set twice - Less readable
    # return "{:.3f}".format(sum(set(array))/len(set(array)))

    # Solution 5 - More Readability
    heights = set(array)
    _sum = sum(heights)
    _len = len(heights)
    avg = _sum/_len
    return avg
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

