import re

txt = '''I am no one and i love nothing.
Why am i here?
I have no idea.'''

print(re.split('\n', txt))
print(re.split('\t', txt))
