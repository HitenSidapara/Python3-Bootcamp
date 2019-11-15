import  re

# #####################################################################################

# def find_number(input):
#     match = re.compile(r'\d{3} \d{3}-\d{4}')
#     res = match.search(input)
#     if res:
#         return res.group()
#     return None


# print(find_number("999 999-2222"))
# print(find_number("999 999-ABCD"))

# #####################################################################################

# def find_allNumber(input):
#     match = re.compile(r'\d{3} \d{3}-\d{4}')
#     res = match.findall(input)
#     if res:
#         return res
#     return None

# print(find_allNumber("333 222-9999 or 123 456-7894"))

# #####################################################################################

# def find_valid(input):
#     match = re.compile(r'^\d{3} \d{3}-\d{4}$')
#     res = match.search(input)
#     if res:
#         return res.group()
#     return None
#
#
# print(find_valid("999 999-2222"))
# print(find_valid(" abc s 999 999-2222 abc"))


# #####################################################################################

# def find_Number(input):
#     match = re.compile(r"\d{3} \d{3}-\d{4}")
#     result = match.fullmatch(input)
#     if result:
#         return True
#     return False
#
# print(find_Number("111 222-3333"))
# print(find_Number("This is my Number 111 222-3333"))
# print(find_Number("111 222-3333 abcdef"))