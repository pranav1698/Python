# You have data inside of a sequence, and need to extract values or reduce the sequence using some criteria.

"""The easiest way to filter sequence data is to use a list comprehension"""
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
[n for n in mylist if n > 0 ]



# You want to make a dictionary that is a subset of another dictionary.

prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}

# This can be achieved by dictionary comprehension
print(prices.items())
p1 = {key:value for key, value in prices.items() if value > 200}

# Making a dictoinary of tech-stacks
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = { key:value for key,value in prices.items() if key in tech_names }

