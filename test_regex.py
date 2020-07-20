import re

regex_pattern = input('Input Pattern: ')
regex_compile = re.compile(regex_pattern)
while True:
    input_str = input('Input String: ')
    match_result = regex_compile.match(input_str)
    if match_result:
        print(match_result.groups())
    else:
        print("Not match")
