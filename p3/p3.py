def get_priority(letter):
	if letter.isupper():
		return ord(letter) - 64 + 26
	else:
		return ord(letter) - 96

def part_one():
	total = 0
	with open('p3.input') as f:
		for line in f.readlines():
			left = line[:len(line)//2]
			right = line[len(line)//2:]
			overlap = set(left) & set(right)
			if len(overlap) != 1:
				raise ValueError(f"overlap wrong size: {len(overlap)}")
			common: str = (set(left) & set(right)).pop()
			priority = get_priority(common)

			if priority > 52 or priority < 1:
				raise ValueError(f"invalid priority: {priority}") 
			total += priority
	return total

def part_two():
	total = 0
	with open('p3.input') as f:
		current_set = set()
		counter = 0
		for line in f.readlines():
			if len(current_set)==0:
				current_set = set(line.strip())
			else:
				current_set = current_set & set(line.strip())
			counter += 1
			if counter == 3:
				total += get_priority(current_set.pop())
				counter = 0
				current_set = set()
	return total

print(part_two())

