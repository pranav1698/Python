# You want to match text using the same wildcard patterns as are commonly used when working in Unix shells (e.g., *.py , Dat[0-9]*.csv , etc.).

"""The fnmatch module provides two functions- fnmatch() and fnmatchcase(), that can be used to perform such matching"""

from fnmatch import fnmatch, fnmatchcase
print fnmatch('foo.txt', '*.txt')
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print [name for name in names if fnmatch(name, 'Dat*.csv')]

# Using fnmatchcase() as it matches cases based on the lower and uppercase conventions
print fnmatchcase('foo.txt', '*.TXT')

# Using regular exressions and the re module
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
# \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
	print True
else:
	print False
#True
if re.match(r'\d+/\d+/\d+', text2):
	print True
else:
	print False
#False
# Using re.compile() we can match a number of strings using the same pattern that will store the pattern in a variable
datepat = re.compile(r'\d+/\d+/\d+')

"""match() always tries to find the match at the start of the string
If you want to search text for all occurrences of a pattern, use the findall() method instead.
findall() is case-insensitive"""
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print datepat.findall(text)
# ['11/27/2012', '3/13/2013']
