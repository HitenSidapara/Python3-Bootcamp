# Create The List


# tasks = ["Learn Python","Learn Java","Learn Node Js",7,17,27,True,False,9.42];
#
# print(tasks);
#
# print(len(tasks));
#
#
# username = ["Hiten Sidapara","Om Khunt","Aarvee Khunt"];
#
# print(username);
# print(len(username));
#
#
#
# number = list(range(1,6));
#
# print(number);
# print(len(number));


# Fetch Data From The List


# numbers = list(range(1, 11));

# print(numbers[0]);
# print(numbers[5]);
# print(numbers[9]);


# Print Data Using The For Loop


# for number in numbers:
#     print(number);


# Using (In) Keyword in list
# in keyword use for the particular data in the list is present or not.


# friends = ["Jay Sidapara", "Kaushik Vasoya", "Prashant Virdiya",
#                "Mayank Sidapara", "Bavin Savliya", "Akshay Padashala",
#                "Raj Chovatiya"];
#
# friend = input("Enter Your Friend Name : ");
#
# while True:
#     if friend in friends:
#         print(f"{friend} is your friend");
#         play_again = input("You Want To play Again?(y/n) : ")
#         if play_again == "y":
#             friend = input("Enter Your Friend Name : ");
#         else:
#             print("Thanks For Playing Game");
#             break;
#     else:
#         print(f"{friend} Is Not Your Best Friend");
#         play_again = input("You Want To play Again?(y/n) : ")
#         if play_again == "y":
#             friend = input("Enter Your Friend Name : ");
#         else:
#             print("Thanks For Playing Game");
#             break;


# Fetch Data using the for and the while loop


# numbers = list(range(1,6));

# print("Data Print Using The For Loop \n");

# for number in numbers:
#     print(number);

#
# print("Data Print Using The While Loop \n");
#
# i=0;
# while i<len(numbers):
#     print(numbers[i]);
#     i+=1;