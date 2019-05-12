# You need to check the start or end of a string for specific text patterns, such as filename extensions, URL schemes, and so on.

# The startswith() and endswith(() methods provide a conveniant way to perform suffix and prefix checking.
filename = 'spam.txt'
print filename.endswith('.txt')
url = 'www.python.org'
print url.startswith('www')

import os
filenames = os.listdir('.')
for name in filenames:
	if name.endswith(('.c', '.h')):
		print name
print any(name.endswith('.py') for name in filenames)

# list of choices
choices = ['http:', 'ftp:']
print tuple(choices)
url = 'http://www.python.org'
print url.startswith(tuple(choices))

filename = 'spam.txt'
print filename[-4:] == '.txt'
url = 'http://www.python.org'
print url[0:4]
print url[:5]

