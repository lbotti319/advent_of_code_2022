import re
def contains(t1, t2) -> bool:
	"""
	t1 contains t2
	"""
	return (t1[0] <= t2[0]) and (t1[1] >= t2[1])

def parse_line(line):
	split = re.split(r",|-", line)
	split = [int(s) for s in split]
	p1 = split[0], split[1]
	p2 = split[2], split[3]

	return p1, p2


def part_one():
	total = 0
	with open('p4.input') as f:
		for line in f.readlines():
			t1, t2 = parse_line(line.strip())
			if contains(t1, t2) or contains(t2, t1):
				total += 1

	return total

print(parse_line("24-66,23-25"))
print(part_one())
