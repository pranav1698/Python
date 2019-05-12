# You want to search for and replace a text pattern in a string.

"""For complicated patterns, we can use the sub() function of the re module.
"""
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
print re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
# Backslashed digits such as \3 refers to capture group numbers in the pattern.
#Again we can use re.complile() for better results, multiple matching

# To know the number of substitutions made in addition to get the replacement text, use re.subn()
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
newtext, n = datepat.subn(r'\3-\1-\2', text)
print newtext
print n
# Today is 2012-11-27. PyCon starts 2013-3-13.
# 2
