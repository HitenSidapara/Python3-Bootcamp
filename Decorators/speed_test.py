from time import time
def speed_test(fun):
    def wrapper(*args,**kwargs):
        start_time = time()
        print(f" Executing {fun.__name__}")
        result = fun(*args,**kwargs)
        end_time = time() -start_time
        print(f"Total Time : {end_time}")
        return result
    return wrapper()

@speed_test
def sum_gen():
    return sum(x for x in range(90000))
@speed_test
def sum_list():
    return sum([x for x in range(90000)])

print(sum_gen)
print(sum_list)