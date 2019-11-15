#  when we are pass the list or tuple it self to the parameter then the we are need to break
#  down so we are use the * in arguments when the function calls.


def sum(*args):
    print(args);
    total =0
    for num in args:
        total+=num;
    print(total);

# pass The Tuple

# data = (1,2,3,4,5,6,7,8,9,10)
# sum(*data);

# sum(*(1,2,3,4,5,6))


# Pass The List

# data = [1,2,3,4,5];
# sum(*data);

# sum(*[1,2,3,4,5,6,7]);