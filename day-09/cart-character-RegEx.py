import re

txt = 'This regular expression example was made on December 6,  2019.'

regex_pattern = r'^This' # ^ means starts with
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern_two = r'[^0-9 ]+' # ^ means negation, no 0 to 9 and spaces.
matches_two = re.findall(regex_pattern_two, txt)
print(matches_two)
