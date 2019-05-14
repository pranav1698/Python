# You have a sequence of items, and you’d like to determine the most frequently occurring items in the sequence.

"""The collectiosn.Counter class is designed for just such a problem 
We can use the most_common() method here, """

words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_counts = Counter(words)
print(word_counts)
top = word_counts.most_common(1)
top_three = word_counts.most_common(3)
print(top)
print(top_three)
word_counts.update(words)
print(word_counts)


# You have a list of dictionaries and you would like to sort the entries according to one or more of the dictionary values.

""" Sorting a list of dictionaries is done using the operator module's itemgetter function. """
rows = [
	{'fname':'Brian', 'lname': 'Jones', 'uid': 1003},
	{'fname':'David', 'lname': 'Beazley', 'uid': 1002},
	{'fname':'John', 'lname': 'Cleese', 'uid': 1001},
	{'fname':'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)

rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)



