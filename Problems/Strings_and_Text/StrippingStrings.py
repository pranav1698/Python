# You want to strip unwanted characters, such as whitespace, from the beginning, end, or middle of a text string.

""" strip() is used to strip characters from the beginning or end of the string,
lstrip() - stripping from the LHS
rstrip() - stripping from the RHS """

# Whitespace stripping
s = '  hello world  \n'
print s.strip()
# 'hello world'
print s.lstrip()
# 'heello world \n'
print s.rstrip()
# '  hello world'

# Character Stripping
t = '-----hello====='
print t.strip('-')
# 'hello====='
print t.strip('-=')
# 'hello'

