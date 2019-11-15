# Example 1 :


# items = dict(name="Aarvee",age=1.1,honest=True);
#
# print(items);
#
# items_update = {key:value for key,value in items.items()};
# print(items_update);


# Example 2 :


# numbers = {
#     "one":1,"second":2,"Third":3
# }
#
# print(numbers);
#
# update_number = {key: values ** 2 for key,values in numbers.items()}
#
# print(update_number);


# Example 3 :


# result = {num:num*2 for num in range(1,6)};
# print(result);
#
# result1 = {num:num*2 for num in [1,2,3,4,5,6,7,8,9,10]};
# print(result1);


# Example 3 :

# str1 = "ABC";
# str2 = "123";
#
# combo = {str1[i]:str2[i] for i in range(0,len(str1))};
# print(combo);




# Example 4 : Conditional Logic

# numbers = [1,2,3,4,5,6,7,8,9,10];
#
# result = {num:("even" if num%2==0 else "odd") for num in numbers};
# print(result);



# Example 5 :

# result = {num:("even" if num%2==0 else "odd") for num in range(1,1001)};
# print(result);



answer = {count: chr(count) for count in range(65,91)}
print(answer);