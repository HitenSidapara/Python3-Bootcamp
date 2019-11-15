import re;

pattern = re.compile(r'\d{3} \d{3}-\d{4}')

# responce = pattern.search("Number is 823 851-9201!")
# Print the match object now extract the value
# print(responce)

# print(responce.group())


res = pattern.findall("my number is 823 851-9201 or 992 551-1618")
# print(res)
# print(type(res))

# print(pattern.findall("my number is 823 851-9201 or 992 551-1618 or 123 456-9874"))