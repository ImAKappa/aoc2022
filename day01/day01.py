from pathlib import Path
from aoc2022.aoc2022 import Day

def part1(day_in: str) -> int:
    """Find Elf with maximum calories"""
    max_cals = 0
    for elf in day_in.split("\n\n"):
        total_calories = sum(int(calorie) for calorie in elf.split("\n") if calorie.isdigit())
        if total_calories > max_cals:
            max_cals = total_calories
    return max_cals

if __name__ == "__main__":
    day = Day(1, Path("./day01"))
    day.test(part1, answer=24000)