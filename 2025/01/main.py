import os

with open(os.path.join(os.path.dirname(__file__), "Input")) as f:
    moves = [line.strip() for line in f if line.strip()]


def part1(start=50, target=0) -> int:
    current = start
    count = 0

    for move in moves:
        direction = move[0]
        value = int(move[1:])

        if direction == "L":
            current = (current + value) % 100
        else:
            current = (current - value) % 100

        if current == target:
            count += 1

    return count


print(f"Part 1: {part1()}")
