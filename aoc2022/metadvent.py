#!/usr/bin/env python3
"""metadvent.py

Module that generates day directories, blank input.txt and test.txt files, and a python file with boilerplate
"""

import argparse
from pathlib import Path
import sys
import io

parser = argparse.ArgumentParser(description='Generate boiler plate directories and code')
parser.add_argument('day', type=int, help='sum the integers (default: find the max)')

args = parser.parse_args()

if __name__ == "__main__":
    day: int = args.day
    # Check if day is witin period of Advent of Code
    if not (1 < day < 25):
        raise ValueError(f"Day should be in interval [1, 25], yet day was {day}")
        
    # Check if day dir already exists
    day_dir = Path(f"day{str(day).zfill(2)}")
    if day_dir in list(Path(".").iterdir()):
        raise FileExistsError(f"{day_dir} already exists!")

    # Make directory
    confirm = input(f"Make {day_dir}? [Y/n]: ")
    if confirm != "Y":
        sys.exit(0)

    day_dir.mkdir(parents=True, exist_ok=True)
    print(f"Created {day_dir.absolute()}")

    # Make blank .txt files
    (day_dir/Path("test.txt")).touch(exist_ok=True)
    print(f"Created blank test.txt")
    (day_dir/Path("input.txt")).touch(exist_ok=True)
    print(f"Created blank input.txt")

    # Make python file
    py_filepath = day_dir/Path(f"{day_dir.name}.py")
    py_filepath.touch(exist_ok=True)
    print(f"Created {py_filepath.absolute()}")

    aoc_boilerplate = f"""from pathlib import Path
from aoc2022.aoc2022 import Day

def part1(day_in: str) -> int:
    return NotImplemented

def part2(day_in: str) -> int:
    return NotImplemented

if __name__ == "__main__":
    {day_dir.name} = Day({day}, Path("./{day_dir.name}"))

    {day_dir}.test(part1, answer=None)
    {day_dir}.solve(part1)
    
    {day_dir}.test(part2, answer=None)
    {day_dir}.solve(part2)"""

    # Add boilerplate to python file
    with io.open(py_filepath, mode="w") as f:
        f.write(aoc_boilerplate)

    print(f"Wrote boilerplate to {py_filepath.absolute()}")

