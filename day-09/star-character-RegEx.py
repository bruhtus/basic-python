import re

regex_pattern = r'[a].*' #. means any character, * means any character zero or more times.
txt = '''Apple and banana are fruits'''

matches = re.findall(regex_pattern, txt)
print(matches)
