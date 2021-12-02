def main():
    part_one()
    part_two()

def part_one():
    nums = read_input() 
    last, *ns = nums
    increases = 0
    for n in ns:
        if n > last:
            increases += 1
        last = n
    print(increases)

def part_two():
    nums = read_input()
    fst, snd, third, *ns = nums
    last_triple = fst + snd + third 
    increases = 0
    for n in ns:
        triple = snd + third + n
        if triple > last_triple:
            increases += 1
        snd = third
        third = n
        last_triple = triple
    print(increases)

def read_input():
    with open('input/day1.txt') as file: 
        lines = file.read().splitlines()
        int_map = map(int, lines)
        return list(int_map)

if __name__ == "__main__":
    main()
