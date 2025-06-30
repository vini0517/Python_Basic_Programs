# For Positive Real Numbers
# Square root of a real number
num = 8
# num = float(input('Enter a number: '))
num_sqrt = num ** 0.5
print(f'The square root of {num:.3f} is {num_sqrt:.3f}')

"""
# For Real or Complex Numbers
#The eval() method can be used to convert complex 
#numbers as input to the complex objects in Python. 

import cmath

num = 1 + 2j
# num = eval(input('Enter a number: '))
num_sqrt = cmath.sqrt(num)
print(f'The square root of {num} is {num_sqrt.real:.3f}+{num_sqrt.imag:.3f}j')

#The square root of (1+2j) is 1.272+0.786j
"""