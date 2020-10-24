import re

regex_pattern = r'[A].' #. means any character except new line.
txt = '''Apple and banana are fruits'''

matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern_two = r'[a].+' #. means any character, + any character one or more times.
matches_two = re.findall(regex_pattern_two, txt)
print(matches_two)
