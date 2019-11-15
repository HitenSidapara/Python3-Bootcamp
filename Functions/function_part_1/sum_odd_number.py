
def sum_of_odd_number(odd_number_list):
    sum=0;
    for odd_number_list in odd_number_list:
        if (odd_number_list % 2) != 0:
            sum+=odd_number_list;
    return sum;

print(sum_of_odd_number([1,2,3,4,5,6,7]));