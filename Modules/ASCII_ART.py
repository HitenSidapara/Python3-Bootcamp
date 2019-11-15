import termcolor;
import pyfiglet;


msg = input("What message do you want to print? ");
color = input("what color ? ").lower();

# Define The Function

def passing(msg,color):
    # pyfiglet.figlet_format(msg, font="banner3-D")
    result = pyfiglet.figlet_format(msg, font="banner3-D")
    termcolor_result = termcolor.colored(result, color=color)
    print(termcolor_result,end="");

# Check The Condition


color_avaiable = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

if color not in color_avaiable:
    color = None;
    passing(msg,color="magenta")
else:
    passing(msg,color)
