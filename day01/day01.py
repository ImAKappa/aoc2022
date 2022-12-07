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

def part2(day_in: str) -> int:
    """Find sum of calories of top three Elves"""
    elves = list()
    for elf in day_in.split("\n\n"):
        total_calories = sum(int(calorie) for calorie in elf.split("\n") if calorie.isdigit())
        elves.append(total_calories)
        elves = sorted(elves, reverse=True)
        while len(elves) > 3:
            elves.pop()
    return sum(elves)

if __name__ == "__main__":
    day01 = Day(1, Path("./day01"))
    day01.test(part1, answer=24000)
    day01.solve(part1)
    day01.test(part2, answer=45000)
    day01.solve(part2)