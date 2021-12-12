def main():
    part_one()
    part_two()

def part_one():
    codes = read_input()
    counts = [0] * len(codes[0])
    for code in codes:
        for i, c in enumerate(code):
            if c == '1':
                counts[i] = counts[i] + 1
    gamma_vals, epsilon_vals = find_diag(counts, len(codes))

    gamma_str = ''.join(gamma_vals)
    epsilon_str = ''.join(epsilon_vals)

    gamma = int(gamma_str, 2)
    epsilon = int(epsilon_str, 2)

    print(gamma * epsilon)



def part_two():
    print("not yet implemented")

def find_diag(counts: [int], code_count: int):
    gamma_bin = []
    epsilon_bin = []
    for c in counts:
        if c > (code_count / 2):
            gamma_bin.append('1')
            epsilon_bin.append('0')
        else:
            gamma_bin.append('0')
            epsilon_bin.append('1')
    return gamma_bin, epsilon_bin


def read_input():
    with open('input/day3.txt') as file: 
        lines = file.read().splitlines()
        char_map = map(list, lines)
        return list(char_map)

def parse_line(line: str):
    tokens = line.split()
    return (tokens[0], int(tokens[1]))

if __name__ == "__main__":
    main()
