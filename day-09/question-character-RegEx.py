import re

txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it email others may write it as Email or E-mail.'''

regex_pattern = r'[Ee]-?mail' #? means here that '-' is optional.

matches = re.findall(regex_pattern, txt)
print(matches)
