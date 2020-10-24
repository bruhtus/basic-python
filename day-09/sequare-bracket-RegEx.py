import re

regex_pattern = r'[Aa]pple | [Bb]anana | [Dd]octor'

txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '

matches = re.findall(regex_pattern, txt)
print(matches)
