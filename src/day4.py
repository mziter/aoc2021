class Board:

    def __init__(self, id, numbers):
        self.id = id
        self.row_marks = [0] * 5
        self.col_marks = [0] * 5
        self.unmarked_sum = 0
        self.numbers = {}
        for ir, row in enumerate(numbers):
            for ic, num in enumerate(row):
                self.numbers[num] = (ir, ic)
                self.unmarked_sum = self.unmarked_sum + num


    def debug(self):
        print('[DEBUG] row_marks:', self.row_marks)
        print('[DEBUG] col_marks:',self.col_marks)
        print('[DEBUG] unmarked_sum:',self.unmarked_sum)
        print('[DEBUG] numbers:',self.numbers)

    def mark(self, number: int) -> bool:
        if number in self.numbers.keys():
            (r, c) = self.numbers[number]
            self.row_marks[r] += 1
            self.col_marks[c] += 1
            self.unmarked_sum -= number
    
    def has_won(self) -> bool:
        for r in self.row_marks:
            if r == 5:
                return True
        
        for c in self.col_marks:
            if c == 5:
                return True
    
    def sum_unmarked(self) -> int:
        return self.unmarked_sum

def part_one():
    nums, boards = parse_input()
    for n in nums:
        for b in boards:
            b.mark(n)
            if b.has_won():
                print('Part One:', n * b.sum_unmarked())
                return

def part_two():
    nums, boards = parse_input()
    known_won = {}
    boards_won = 0
    for n in nums:
        for b in boards:
            if b.id not in known_won.keys():
                b.mark(n)
                if b.has_won():
                    known_won[b.id] = True
                    boards_won += 1
                if boards_won == len(boards):
                    print('Part Two: ', n * b.sum_unmarked())
                    return

def read_input_lines() -> [str]:
    with open('input/day4.txt') as file: 
        return file.read().splitlines()

def parse_input():
    lines = read_input_lines()
    marks = list(map(int, lines[0].split(',')))

    board_input = lines[2:]
    nums_lines = list(map(split_and_parse, board_input))

    boards = []
    i = 0
    id = 1
    while i <= len(board_input):
        boards.append(Board(id, [
            nums_lines[i],
            nums_lines[i+1],
            nums_lines[i+2],
            nums_lines[i+3],
            nums_lines[i+4],
        ]))
        i += 6
        id += 1

    return marks, boards

def split_and_parse(line: str) -> [int]:
    num_strs = line.split()
    return list(map(int, num_strs))

def test():
    test_board = [
        [14, 21, 17, 24, 4],
        [10, 16, 15,  9, 19],
        [18, 8, 23, 26, 20],
        [22, 11, 13, 6, 5],
        [2, 0, 12, 3, 7]]

    b = Board(1, test_board)
    marks = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

    answer = 0
    for n in marks:
        b.mark(n)
        if b.has_won():
            answer = n
            break
    assert answer == 24
    assert b.sum_unmarked() == 188

def main():
    test()
    part_one()
    part_two()
    
if __name__ == "__main__":
    main()