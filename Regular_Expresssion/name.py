import re

def parse_name(input):
    valid_name = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
    result = valid_name.search(input);
    print(result.group())
    print(result.groups())
    # 1st Way
    print(result.group(2))
    print(result.group(3))
    # 2nd Way Using The regular expression lable ?P<first> ?P<last>
    print(result.group('first'))
    print(result.group('last'))


parse_name("Mr. Hiten Sidapara")