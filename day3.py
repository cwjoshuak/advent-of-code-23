
import string
from collections import defaultdict
def p1():
    part_numbers = []
    nums = defaultdict(dict)
    symbols = []
    with open('./data/day3.txt') as f:
        data = f.read().split('\n')
        for x_idx, line in enumerate(data):
            for y_idx, char in enumerate(line):
                if char.isdigit():
                    nums[x_idx][y_idx] = (char, False)
                if char in string.punctuation and char != ".":
                    symbols.append((x_idx, y_idx, char))
        for symbol in symbols:
            x, y, char = symbol
            for x_idx in range(x-1, x+2):
                for y_idx in range(y-1, y+2):
                    if x_idx in nums and y_idx in nums[x_idx]:
                        nums[x_idx][y_idx] = (nums[x_idx][y_idx][0], True)

        for x_idx in nums:
            num = ''
            curr_y = -1
            is_part_number = False
            for y_idx in nums[x_idx]:
                char, should_add = nums[x_idx][y_idx]
                if curr_y != -1 and y_idx != curr_y + 1:
                    if is_part_number:
                        part_numbers.append(int(num))
                    is_part_number = False
                    num = ''
                    curr_y = -1
                if curr_y == -1 or y_idx == curr_y + 1:
                    curr_y = y_idx
                    num += char
                    if should_add:
                        is_part_number = True
            if num != '' and is_part_number:
                part_numbers.append(int(num))

        print(sum(part_numbers))


def p2():
    part_numbers = []
    nums = defaultdict(dict)
    symbols = []
    with open('./data/day3.txt') as f:
        data = f.read().split('\n')
        for x_idx, line in enumerate(data):
            for y_idx, char in enumerate(line):
                if char.isdigit():
                    nums[x_idx][y_idx] = (char, False, set())
                if char in string.punctuation and char != ".":
                    symbols.append((x_idx, y_idx, char))
        for symbol in symbols:
            x, y, char = symbol
            for x_idx in range(x-1, x+2):
                for y_idx in range(y-1, y+2):
                    if x_idx in nums and y_idx in nums[x_idx]:
                        nums[x_idx][y_idx][2].add((x, y))
                        nums[x_idx][y_idx] = (nums[x_idx][y_idx][0], True, nums[x_idx][y_idx][2])

        for x_idx in nums:
            num = ''
            curr_y = -1
            is_part_number = False
            connected_symbols = set()
            for y_idx in nums[x_idx]:
                char, should_add, connected_symbol = nums[x_idx][y_idx]
                if curr_y != -1 and y_idx != curr_y + 1:
                    if is_part_number:
                        part_numbers.append((int(num), connected_symbols))
                    is_part_number = False
                    num = ''
                    curr_y = -1
                    connected_symbols = set()
                if curr_y == -1 or y_idx == curr_y + 1:
                    curr_y = y_idx
                    num += char
                    connected_symbols.update(connected_symbol)
                    if should_add:
                        is_part_number = True
            if num != '' and is_part_number:
                part_numbers.append((int(num), connected_symbols))

        sum = 0
        for symbol in symbols:
            xs, ys, char = symbol
            ratio = 1
            li = [i for i in filter(lambda x: (xs,ys) in x[1], part_numbers)]
            if len(li) < 2: continue
            for i in li:
                ratio *= i[0]
            sum += ratio
        print(sum)
