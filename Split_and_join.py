# https://www.hackerrank.com/challenges/python-string-split-and-join/problem


def split_and_join(line):
    # Solution 1 - Poor performance 
         # replace actually creates 2 objects in memory. 
         
    # return line.replace(' ', '-')
    #----------------------------------------
    
    # Solution 2 - Good performance with better readability
         # Split/join perform operations in-place, therefore from a performance point of view you're better off with split()-join()
         # method both objects are not in the memory at the same time. Join() method is executed after the Split() method is done executing.
        
    # split_line = line.split()
    # joined_line = '-'.join(split_line)
    # return joined_line 
    #------------------------------------
    
    # Solution 3 - 1 line - Simple, 1 line Elegant solution - Good performance 
    return '-'.join(line.split())
    #------------------------------------
    
# Solution 4 - Elegant one line solution
# print(*input().split(), sep='-')
    # input.split() returns a list of words. 
    # so we use * to unpack the values. eg: words = 'hello world'.split(). 
    # Here words = ['hello', 'world']
    # print(*words) will print `hello world'.



if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
