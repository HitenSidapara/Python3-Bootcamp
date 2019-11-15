import re

url_regx = re.compile(r'(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')

result = url_regx.search("https://www.google.com/search?q=india+flag+images&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi01J7hycLgAhWMfSsKHXxfCrAQ_AUIDigB&biw=1366&bih=637")

# print(result.group())
# print(result.groups())

print(f"If Put 0 in the Bracket : {result.group(0)}")
print(f"Protocol : {result.group(1)}")
print(f"Domain Name : {result.group(2)}")
print(f"After else : {result.group(3)}")