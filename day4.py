def p1():
    with open("./data/day4.txt") as f:
        lines = f.read().split("\n")
        sum = 0
        for line in lines:
            if len(line.strip()) == 0: continue
            card, numbers = line.split(": ")
            winning, numbers = numbers.split(" | ")
            winning = set([int(i) for i in winning.split(" ") if i != ""])
            numbers = set([int(i) for i in numbers.split(" ") if i != ""])
            winners = winning.intersection(numbers)
            if len(winners) == 0: continue
            else: 
                sum += pow(2, len(winners) - 1)
        print(sum)

def p2():
    with open("./data/day4.txt") as f:
        lines = f.read().split("\n")

        cards = [1 for i in lines if i.strip() != ""]
        for idx, line in enumerate(lines):
            if len(line.strip()) == 0: continue
            card, numbers = line.split(": ")
            winning, numbers = numbers.split(" | ")
            winning = set([int(i) for i in winning.split(" ") if i != ""])
            numbers = set([int(i) for i in numbers.split(" ") if i != ""])
            winners = winning.intersection(numbers)
            
            if len(winners) == 0: continue
            else:
                for i in range(idx + 1, idx + 1 + len(winners) ):
                    cards[i] += 1 * cards[idx]
        print(sum(cards))