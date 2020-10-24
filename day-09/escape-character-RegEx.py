import re

regex_pattern = r'\d' #d is a special character which means digits.
txt = 'This regular expression example was made on December 6,  2019.'

matches = re.findall(regex_pattern, txt)
print(matches)
