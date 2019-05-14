# You have an N-element tuple or sequence that you would like to unpack into a collection of N variables.

"""Any sequence can be unpacked into variables using a assignment operation.
THe number of variables and structure match the sequence
"""
p = (4,5)
x,y = p
print(x)
print(y)
# It works for strings also

s = 'Hello'
a, b, c, d, e = s
print(c)
# >> l

""" You can discard certain values, we can use a throwaway variable name for the same """
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_, shares, price, _ = data
print(shares)

"""You need to unpack N elements from an iterable, but the iterable may be longer than N
elements, causing a “too many values to unpack” exception."""
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(phone_numbers)
# >> ['773-555-1212', '847-555-1212']
"""Elements with star expressions will always be a list, even if one value is assigned.
iterating over a sequence of tuples of varying length
"""
records = [
	('foo', 1, 2),
	('bar', 'hello'),
	('foo', 3, 4),
]

def do_foo(x, y):
	print('foo', x, y)
def do_bar(s):
	print('bar', s)

for tag,*args in records:
	if tag == "foo":
		do_foo(*args)
	elif tag == "bar":
		do_bar(*args)

# Using throwaways with star expressions also:
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_ , (*_, year) = record
print(year)

