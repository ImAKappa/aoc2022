# --- Day 3: Rucksack Reorganization ---
# Completed: Dec 08, 2022

from pathlib import Path
from aoc2022.aoc2022 import Day

def part1(day_in: str) -> int:
    """Finds the item type that appears in both compartments of each rucksack. 
    Calculates the sum of the priorities of those item types
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    priority_map = {letter:i+1 for i, letter in enumerate([*list(alphabet), *list(alphabet.upper())])}
    total_sum = 0
    for rucksack in day_in.splitlines():
        # Split rucksack into two compartments
        midpoint = len(rucksack) // 2
        compart_one = set(rucksack[:midpoint]) 
        compart_two = set(rucksack[midpoint:])
        # Find common item
        common_item, = compart_one.intersection(compart_two)
        assert len(common_item) == 1
        # Calculate priority
        priority = priority_map[common_item]
        total_sum += priority
    return total_sum

def part2(day_in: str) -> int:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    priority_map = {letter:i+1 for i, letter in enumerate([*list(alphabet), *list(alphabet.upper())])}
    total_sum = 0
    elf_groups = day_in.splitlines()
    group_size = 3
    for i in range(0, len(elf_groups), group_size):
        # Get rucksacks in elf group
        ruck_1 = set(elf_groups[i])
        ruck_2 = set(elf_groups[i+1])
        ruck_3 = set(elf_groups[i+2])
        # Find common item
        common_item, = ruck_1.intersection(ruck_2.intersection(ruck_3))
        assert len(common_item) == 1
        # Calculate priority
        priority = priority_map[common_item]
        total_sum += priority
    return total_sum

if __name__ == "__main__":
    day03 = Day(3, Path("./day03"))

    day03.test(part1, answer=157)
    day03.solve(part1)
    
    day03.test(part2, answer=70)
    day03.solve(part2)