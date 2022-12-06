import heapq

def main():
    fat_elves = []
    current_elf = 1
    with open("p1.input") as f:
        elf_total = 0
        for line in f.readlines():
            if line != "\n":
                elf_total += int(line)
            else:
                if len(fat_elves) == 3:
                    heapq.heappushpop(fat_elves, (elf_total, current_elf))
                else:
                    heapq.heappush(fat_elves, (elf_total, current_elf))
                elf_total = 0
                current_elf += 1
    print(fat_elves)
    total_calories = sum([elf[0] for elf in fat_elves])
    print(total_calories)
    return fat_elves

if __name__ == '__main__':
    main()