import re
titles = [
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "The Days of Anna Madrigal (2014)",
    "Mary Ann in Autumn (2010)",
    "Further Tales of the City (1982)",
    "Babycakes (1984)",
    "More Tales of the City (1980)",
    "Sure of You (1989)",
    "Michael Tolliver Lives (2007)"
]

titles.sort()
print(titles)
number_shored_list = []


pattern = re.compile(r'(?P<title>^[\w ]+) \((?P<date>\d{4})\)')

for titles in titles:
    result  = pattern.sub("\g<date> \g<title>", titles)
    number_shored_list.append(result)

number_shored_list.sort()
for data in number_shored_list:
    print(data)
