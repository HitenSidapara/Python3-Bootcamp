import re

text = "My name is Mr. Hiten and my friend name is Mr. Om Khunt and Mr. Raj Chovatiya"

pattern = re.compile(r'(Mr\.|Mrs\.|Miss\.) ([a-z])[a-z]+', re.IGNORECASE);

# result = pattern.search(text)

# print(result.group())

result = pattern.sub("\g<1> \g<2>",text)

print(result)
