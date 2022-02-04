import numpy

# 1. Read input
# 2. convert to numpy array
# 3. print ceil, floor, rint using numpy method

# Solution
# numpy.set_printoptions(sign=' ')
# input_array = numpy.array(list(map(float,input().split())))
# print(numpy.floor(input_array))
# print(numpy.ceil(input_array))
# print(numpy.rint(input_array))

# Solution 2
# numpy.set_printoptions(sign=' ')
# input_array = numpy.array(input().split(), float)
# print(numpy.floor(input_array), numpy.ceil(input_array), numpy.rint(input_array), sep='\n')

numpy.set_printoptions(legacy='1.13')
input_array = numpy.array(input().split(), float)
print(numpy.floor(input_array), numpy.ceil(input_array), numpy.rint(input_array), sep='\n')
