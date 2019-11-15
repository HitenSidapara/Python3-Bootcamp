# Command to check the doctest
# python3 -m doctest -v doctest_demo.py

# Example : 1

# def add(a,b):
#     """
# 	>>> add(2, 3)
# 	5
# 	>>> add(100,200)
# 	300
#     """
#     return a+b
#     # return a*b



# Example 2

# def say_hi():
#     """
#     >>> say_hi()
#     'hi'
#
#     """
#     return "hi"




# Example 3 :

def double(value):
    """
    >>> double([1,2,3,4])
    [2, 4, 6, 8]

    >>> double([])
    []

    >>> double(['a','b','c','d'])
    ['aa', 'bb', 'cc', 'dd']

    >>> double([True, None])
	Traceback (most recent call last):
		...
	TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """

    return [2 * i for i in value]