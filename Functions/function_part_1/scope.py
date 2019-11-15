# 1. global scope

# total = 0;
# def increment():
#     global total;
#     total+=1;
#     return total;
#
# print(increment());



# 2. nonlocal scope

def outer():
    counter = 0
    def inner():
        nonlocal counter;
        counter= counter+1000;
        print(counter);
    return inner();

outer();