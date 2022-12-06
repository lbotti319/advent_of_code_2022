from collections import deque
def part_one():
	with open('p6.input') as f:
		stream = f.read().strip()
		current_buffer = deque(list(stream[:4]))
		c_count = 4
		while len(set(current_buffer)) != 4:
			current_buffer.popleft()
			current_buffer.append(stream[c_count])
			c_count += 1
	return c_count
print(part_one())


def part_two():
	with open('p6.input') as f:
		stream = f.read().strip()
		current_buffer = deque(list(stream[:14]))
		c_count = 14
		while len(set(current_buffer)) != 14:
			current_buffer.popleft()
			current_buffer.append(stream[c_count])
			c_count += 1
	return c_count
print(part_two())