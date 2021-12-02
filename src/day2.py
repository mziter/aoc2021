def main():
    part_one()

def part_one():
    instructions = read_input()
    horizontal = 0
    depth = 0
    for i in instructions:
        (direction, magnitude) = i
        if direction == 'forward':
            horizontal += magnitude
        if direction == 'up':
            depth -= magnitude
        if direction == 'down':
            depth += magnitude
    print(horizontal * depth)

def part_one():
    instructions = read_input()
    horizontal = 0
    depth = 0
    aim = 0
    for i in instructions:
        (direction, magnitude) = i
        if direction == 'forward':
            horizontal += magnitude
            depth += aim * magnitude
        if direction == 'up':
            aim -= magnitude
        if direction == 'down':
            aim += magnitude
    print(horizontal * depth)

def read_input():
    with open('input/day2.txt') as file: 
        lines = file.read().splitlines()
        int_map = map(parse_line, lines)
        return list(int_map)

def parse_line(line: str):
    tokens = line.split()
    return (tokens[0], int(tokens[1]))

if __name__ == "__main__":
    main()
