# Error in python
# NameError
# SyntaxError
# VlaueError
# TypeEoor

# showing this message in the error field

# raise NameError("This is the name error generated")

# raise  SyntaxError("Please Check Your Syntax")



# Exmaple  :


def colorize(text,color):

    colors = ("red","white","yellow","blue","green")
    if type(text) is not str:
        raise TypeError("Enter The String Value")
    if color not in colors:
        raise ValueError("color is not avaiable")

    print(f"{text} = {color}")


colorize("hi","white")
colorize(1,"white")
colorize("Hello","Cyan")
