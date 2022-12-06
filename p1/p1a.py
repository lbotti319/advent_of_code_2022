def main():
    current_max = 0
    max_elf = 0
    current_elf = 1
    with open("p1.input") as f:
        elf_total = 0
        for line in f.readlines():
            if line != "\n":
                elf_total += int(line)
            else:
                if elf_total >= current_max:
                    current_max = elf_total
                    max_elf = current_elf
                elf_total = 0
                current_elf += 1
    print(max_elf, current_max, current_elf)
    return max_elf



if __name__ == '__main__':
    main()