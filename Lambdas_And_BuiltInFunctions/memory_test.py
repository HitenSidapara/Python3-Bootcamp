# list comprehension vs generators
# generators have lighter than the list comprehensive
# if we are store data and iterate the data then use the list comprehensive
# otherwise passing data direct to the fun so use the generators


import sys

list = sys.getsizeof([num * 10 for num in range(1000)]);
generators = sys.getsizeof(num * 10 for num in range(1000))

print(f"list comprehensive takes {list} bytes");
print(f"gererators takes {generators} bytes");