

def for_loop(iterable,func):
    result = iter(iterable)

    while True:
        try:
            data=next(result)
            # print(data)
        except StopIteration:
            break
        else:
            func(data)

def Square(data):
    print (data*data)

# for_loop("Hiten")
for_loop([1,2,3,4,5],Square)
for_loop([1,2,3,4,5],print)
