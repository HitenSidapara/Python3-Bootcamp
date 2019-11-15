# external lib.

import termcolor

# print(dir(termcolor));
# print(help(termcolor))


color_cyan = termcolor.colored("Om Khunt", color="cyan")
print(color_cyan)

color_blink = termcolor.colored("Om Khunt", color="yellow",on_color="on_cyan",attrs=["blink"])

print(color_blink)


color_reversed = termcolor.colored("Om Khunt", color="yellow",on_color="on_cyan",attrs=["blink","reverse"])

print(color_reversed)