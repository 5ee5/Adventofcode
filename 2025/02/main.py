import os

def load_raw():
    path = os.path.join(os.path.dirname(__file__), "Input")
    with open(path) as f:
        return f.read().strip()


def parse_ranges(raw: str):
    raw = raw.replace("\n", "")
    parts = raw.split(",")

    ranges = []
    for p in parts:
        if not p.strip():
            continue
        a, b = p.split("-")
        ranges.append((int(a), int(b)))
    return ranges


def is_repeated_twice(n: int) -> bool:
    s = str(n)

    if s[0] == "0":
        return False

    if len(s) % 2 != 0:
        return False

    half = len(s) // 2
    return s[:half] == s[half:]


def part1(ranges) -> int:
    total = 0

    for start, end in ranges:
        for n in range(start, end + 1):
            if is_repeated_twice(n):
                total += n

    return total


def is_repeated_at_least_twice(n: int) -> bool:
    s = str(n)

    if s[0] == "0":
        return False

    L = len(s)

    for size in range(1, L // 2 + 1):
        if L % size != 0:
            continue

        chunk = s[:size]
        repeats = L // size

        if chunk * repeats == s:
            return True

    return False


def part2(ranges) -> int:
    total = 0

    for start, end in ranges:
        for n in range(start, end + 1):
            if is_repeated_at_least_twice(n):
                total += n

    return total


if __name__ == "__main__":
    raw = load_raw()
    ranges = parse_ranges(raw)

    print(f"Part 1: {part1(ranges)} \nPart 2: {part2(ranges)}")
