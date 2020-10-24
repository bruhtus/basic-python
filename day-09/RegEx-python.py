import re

txt = 'why am i here?'
txt_two = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

#re.match(substring, string, re.I) -> substring is a pattern, string is the text we look for a pattern, re.I is case ignore flag.
match = re.match('why am', txt, re.I) #must start from beginning, return only if the text start with the pattern.
print(match)

span = match.span()
print(span)

start, end = span
print(start, end)

substring = txt[3] #could be [start:end] or something like that.
print(substring)

substring_1 = txt[4:end] #could be [start:end] or something like that.
print(substring_1)

match_two = re.search('first', txt_two, re.I)
print(match_two)

print(f'substring text two: {txt_two[101]}\n')

matches = re.findall('python', txt_two, re.I)
print(f'using re.findall and return all the search results as a string: {matches}')

matches_two = re.findall('[Pp]ython', txt_two) #without re.I to show uppercase and lower case
print(f'using re.findall and return all the search results as a string: {matches_two}')

replace_substring = re.sub('Python|python', 'Javascript', txt_two, re.I)
print(f'replace substring uppercase and lowercase: {replace_substring}')
