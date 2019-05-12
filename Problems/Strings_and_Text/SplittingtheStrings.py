# You need to split the string to fields, but the delimiters (and spacing around them) aren't consistent

"""The split() method of string is meant for very simple cases, and does not allow for multiple delimiters
or account for possible around the delimiters."""

line = 'asdf fjdk; afed, fjek,asdf,   foo'
import re
line_1 = re.split(r'[;,\s]\s*', line)
print line_1
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
"""re.split() function is a useful function to specify multiple pattern for the seperator.
We use it for flexiblity, In the solution the seperator is a comma, a semicolor, or whitespace
and followed by other amount of extra whitespace, whenever you find the pattern the entire match becomes the 
delimiter between whatever fields lie on the either side of the match.
Be caredul if the regular expression that involve a capture group enclosed in parentheses, capture groups used 
makes the matches text is also included in the result
"""
line_2 = re.split(r'(;|,|\s)\s*', line)
print line_2
values = line_2[::2]
print line_2
delimiters = line_2[1::2] + ['']
print delimiters

# Reform the line without using the delimiters
print ' '.join(line_1)
# Reform the line using the same delimiters
print ''.join(v+d for v,d in zip(values, delimiters))
"""We don't want the seperator characters, but still need to use parentheses to group parts of the regular 
expression pattern, make sure we use a non-capture group (?:...)"""
line_3 = re.split(r'(?:,|;|\s)\s*', line)
print line_3
