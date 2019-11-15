# zip()

# num1 = [1,2,3,4,5]
# num2 = [6,7,8,9,10]
#
# print(list(zip(num1,num2)));
# print(list(zip(num2,num1)));
# print(dict(zip(num1,num2)));
#
# fname = ["hiten","om","raj","akshay"];
# lname = ["sidapara","khunt","chovatiya","padashala"]
#
# print(list(zip(fname,lname)));
# print(dict(zip(fname,lname)));



# Exercise :

midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']

# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}
print(final_grades)

# Another Way
final_grades1 = zip(
    students,
    map(lambda pairs: max(pairs),
    zip(midterms,finals)
    )
)
print(dict(final_grades1));


# avg score

avg_grade = zip(
    students,
    map(lambda pairs: (pairs[0]+pairs[1])/2,
    zip(midterms,finals)
    )
)

print(dict(avg_grade));