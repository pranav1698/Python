# You want to make a list of the largest or smallest N items in a collection.

#The heapq has two functions nlargest() and nsmallest()

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]

# ** 
portfolio = [
	{'name':'IBM', 'shares': 100, 'price': 91.1},
	{'name':'AAPL', 'shares': 50, 'price': 543.22},
	{'name':'FB', 'shares': 200, 'price': 21.09},
	{'name':'YHOO', 'shares': 45, 'price': 16.35},
	{'name':'ACME', 'shar':75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(cheap, expensive)

""" The most important feature of the hwap is that heap[0] is always the smallest item in the 
collection. Subsequent elements can be found out using the heap.heappop() method"""

