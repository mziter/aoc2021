def main() -> None:
    test_examples()
    part_one()
    part_two()

def part_one() -> None:
    codes = read_input_chars()
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

def part_two() -> None:
    codes = read_input_lines()
    print(oxygen_generator_rating(codes, 0) * co2_scrubber_rating(codes, 0))

def oxygen_generator_rating(codes: [str], idx: int) -> int:
    if len(codes) == 1:
        binary_int = int(codes[0], 2)
        return binary_int 
    count_ones = 0
    for code in codes:
        if code[idx] == '1':
            count_ones += 1
    most_common = '1' if (count_ones >= len(codes) / 2) else '0'
    filtered = []
    for code in codes:
        if code[idx] == most_common:
            filtered.append(code)
    return oxygen_generator_rating(filtered, idx + 1)

def co2_scrubber_rating(codes: [str], idx: int) -> int:
    if len(codes) == 1:
        binary_int = int(codes[0], 2)
        return binary_int 
    count_zeros = 0
    for code in codes:
        if code[idx] == '0':
            count_zeros += 1
    least_common = '1' if (count_zeros > len(codes) / 2) else '0'
    filtered = []
    for code in codes:
        if code[idx] == least_common:
            filtered.append(code)
    return co2_scrubber_rating(filtered, idx + 1)

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


def read_input_chars() -> [[chr]]:
        lines = read_input_lines() 
        char_map = map(list, lines)
        return list(char_map)

def read_input_lines() -> [str]:
    with open('input/day3.txt') as file: 
        return file.read().splitlines()

def test_examples() -> None:
    input = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010']
    
    oxy_result = oxygen_generator_rating(input, 0)
    assert oxy_result == 23

    co2_result = co2_scrubber_rating(input, 0)
    assert co2_result == 10

if __name__ == "__main__":
    main()
