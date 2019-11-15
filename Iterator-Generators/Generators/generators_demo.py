
# Generator define using the generator function
# yield keyword is used to the return data number of times
# if the data needed

def counter_number(max):
    counter = 1
    while counter <= max:
        # yield keyword is used to the create the generators
        yield counter
        counter += 1


c = counter_number(5)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

cc = counter_number(3)
print(list(cc))

forloop = counter_number(100)

for i in forloop:
    print(i)

donderd = counter_number(2)
print(donderd.__next__())
print(donderd.__next__())