from pathlib import Path
from aoc2022.aoc2022 import Day

def part1(day_in: str) -> int:
    return NotImplemented

def part2(day_in: str) -> int:
    return NotImplemented

if __name__ == "__main__":
    day02 = Day(2, Path("./day02"))

    day02.test(part1, answer=None)
    day02.solve(part1)
    
    day02.test(part2, answer=None)
    day02.solve(part2)