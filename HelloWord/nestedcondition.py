print("Enter Your Age : ");
age = input();

if age:
    age = int(age)
    if age>=21:
        print(f"Your age {age} (grater than equla 21)");
    elif age >=18:
        print(f"Your age {age} (grater than or equla 18)");
    else:
        print("You are to young");
else:
    print("Your Are Enter Empty String");