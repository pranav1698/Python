# You need to search for and possibly replace text in a case-insensitive manner.

text = 'UPPER PYTHON, lower python, Mixed Python'
import re
print re.sub('python', 'snake', text)
# UPPER PYTHON, lower snake, Mixed Python
print re.sub('python', 'snake', text, flags=re.IGNORECASE)
# UPPER snake, lower snake, Mixed snake
print re.sub('Python', 'snake', text, flags=re.IGNORECASE)
# UPPER snake, lower snake, Mixed snake
print re.sub('Python', 'snake', text)
# UPPER snake, lower snake, Mixed snake

