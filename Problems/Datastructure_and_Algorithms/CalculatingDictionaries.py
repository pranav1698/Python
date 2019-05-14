# You want to perform various calculations (e.g., minimum value, maximum value, sorting, etc.) on a dictionary of data.

prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}

a = sorted(zip(prices.values(), prices.keys()))
print(a)

""" The zip() inverts the dictionary into a sequence of (value, key) pairs"""

# You have two dictionaries and want to find out what they might have in common (same keys, same values, etc.).
a = {
'x' : 1,
'y' : 2,
'z' : 3
}

b = {
'w' : 10,
'x' : 11,
'y' : 2
}

# Set operations are applied to dictionaries
a.keys() & b.keys() # {'x', 'y'}
a.keys() - b.keys() # {'z'}
a.items() & b.items() # {'y': 2}
""" ** In part, this is due to the fact that unlike keys, the items
contained in a values view aren’t guaranteed to be unique. This alone makes certain set
operations of questionable utility """

# You want to eliminate the duplicate values in a sequence, but preserve the order of the remaining items.