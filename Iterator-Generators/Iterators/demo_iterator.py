
# Difference between the iterator and iterable
# String list dict are all the iterable there are not direct use of the next() method
# next() method gives the StopIteration when the value are not avaiable

name = iter("Hiten")
print(next(name))
print(next(name))
print(next(name))
print(next(name))
print(next(name))
# print(next(name))

print("*************************")
list = iter(list(range(1,11)))
print(next(list))
print(next(list))
print(next(list))
print(next(list))
print(next(list))
print(next(list))
print(next(list))
print(next(list))
print(next(list))
print(next(list))
print(next(list))