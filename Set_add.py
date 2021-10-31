# Apply your knowledge of the .add() operation to help your friend Rupal.

# Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of  country stamps.

# Find the total number of distinct country stamps.

# Input Format
#   The first line contains an integer , the total number of country stamps.
#   The next  lines contains the name of the country where the stamp is from.
  
# Constraints
#  1<n<1000
  
# Output Format
#   Output the total number of distinct country stamps on a single line.
  
  
# Sample input
# 7
# UK
# China
# USA
# France
# New Zealand
# UK
# France 

# Sample output
# 5


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    # n_stamps = int(input())
    stamp_set = set()
    # Solution 1
    # for i in range(n_stamps):
    #     stamp_set.add(input())
    # print(len(stamp_set))
    
    # Solution 2
    # [stamp_set.add(input()) for i in range(n_stamps)]
    # print(len(stamp_set))

    # Solution 3 - using set()
    # print(len(set([str(input()) for i in range(int(input()))])))
    
    #Solution 4 - Using {}
    print(len({str(input()) for x in range(int(input()))}))
