# You want to keep a limited history of the last few items seen during iteration or during some other kind of processing.

""" ** The following code performs a simple text match on a sequence of olines and yeilds the matching line
along with previous N lines of context """

from collections import deque

def search(lines, pattern, history=5):
	previous_lines = deque(maxlen=history)
	for line in lines:
		if pattern in line:
			yield line, previous_lines
		previous_lines.append(line)

# Example use on a file
	with open('somefile.txt') as f:
		for line, prevlines in search(f, 'python', 5):
			for pline in prevlines:
				print(pline, end='')
			print(line, end='')
			print('-'*20)

""" Using deque(maxlen=N) creates a fixed size queue. When new items are added and the queue is full
the oldest items are automatically removed """

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q
# >> deque([1, 2, 3], maxlen=3)
q.append(4)
q
# >> deque([2, 3, 4], maxlen=3)
