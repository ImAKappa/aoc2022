from pathlib import Path
from aoc2022.aoc2022 import Day
from typing import Self

class Interval:

    def __init__(self, interval: str):
        """
        Params:
            interval: 'NUMBER-NUMBER'
        '"""
        a, b = interval.split("-")
        self.a = int(a)
        self.b = int(b)

    def is_subrange_of(self, other: Self):
        """Whether range1 is a subset of range2"""
        return other.a <= self.a and self.b <= other.b
    
    def overlaps(self, other: Self):
        """Test if self interval overlaps other interval"""
        return self.a <= other.b and self.b >= other.a

def part1(day_in: str) -> int:
    """Calculates how many assignment pairs have one range fully contained in the other"""
    total_pairs = 0
    for pair in day_in.splitlines():
        first, second = pair.split(",")
        range_1, range_2 = Interval(first), Interval(second)
        if range_1.is_subrange_of(range_2) or range_2.is_subrange_of(range_1):
            total_pairs += 1
    return total_pairs

def part2(day_in: str) -> int:
    """Calculates how many assignment pairs have ranges that overlap"""
    total_pairs = 0
    for pair in day_in.splitlines():
        first, second = pair.split(",")
        range_1, range_2 = Interval(first), Interval(second)
        if range_1.overlaps(range_2):
            total_pairs += 1
    return total_pairs

if __name__ == "__main__":
    day04 = Day(4, Path("./day04"))

    day04.test(part1, answer=2)
    day04.solve(part1)
    
    day04.test(part2, answer=4)
    day04.solve(part2)