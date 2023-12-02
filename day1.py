def p1():
    sum = 0

    with open('./data/day1.txt') as f:
        data = f.read().split('\n')
        for line in data:
            nums = [c for c in line.strip() if c.isdigit()]
            if len(nums) == 0:
                continue
            firstNum = nums[0]
            lastNum = nums[-1]
            sum += int(''.join([firstNum, lastNum]))
    print(sum)

NUMS = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

import re
def p2():
    regex = re.compile(r'(\d|zero|one|two|three|four|five|six|seven|eight|nine)')
    reverse_regex = re.compile(r'(\d|orez|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)')
    sum = 0

    with open('./data/day1.txt') as f:
        data = f.read().split('\n')
        for line in data:
            ltr = regex.findall(line)
            rtl = reverse_regex.findall(line[::-1])
            ltr_nums = list(map(lambda x: x if x.isdigit() else NUMS[x], ltr))
            rtl_nums = list(map(lambda x: x if x.isdigit() else NUMS[x[::-1]], rtl))

            if len(ltr) == 0:
                continue
            print(int(''.join([ltr_nums[0], rtl_nums[0]])))
            sum += int(''.join([ltr_nums[0], rtl_nums[0]]))
    print(sum)

