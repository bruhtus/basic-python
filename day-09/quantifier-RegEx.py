import re

txt = 'This regular expression example was made on December 6,  2019.'

regex_pattern = r'\d{1,4}' #exactly one and four digits.
matches = re.findall(regex_pattern, txt)
print(matches)
