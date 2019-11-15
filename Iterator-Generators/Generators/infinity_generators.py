def count_beat():
    num = (1,2,3,4)
    count = 1
    while True:
        if count > len(num) : count=1
        yield count
        count +=1

c = count_beat()
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

for i in count_beat():
    print(i)
    print(i)