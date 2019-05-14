# You want to make a dictionary that maps keys to more than one value (a so-called “multidict”).

""" To easilly construct multidicts, we can default dict in the collections module"""

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)

e = defaultdict(set)
e['a'].add(1)
e['a'].add(2)
e['b'].add(4)
print(e)


# You want to create a dictionary, and you also want to control the order of items when iterating or serializing.

""" To control the order of items in the dictionary, you can use OrderedDict from collections module """
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
print(d)

for key in d:
	print (d[key])