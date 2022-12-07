#!/usr/bin/env python3
"""aoc2022.py

Helper/convenience methods for Advent of Code 2022
"""

from pathlib import Path
import io

class Day:
    """Class that manages input for the problem of the day"""

    def __init__(self, day: int, parent_dir: Path):
        if not isinstance(day, int):
            raise ValueError(f"`day` should be an int, but is instead {type(day)}")
        self.day = day
        self.parent_dir = parent_dir
        self.test_input = self.get_test_input()
        self.full_input = self.get_full_input()

    def __repr__(self):
        return f"Day(day={self.day})"

    def __str__(self):
        return f"Day {self.day}" 

    def get_test_input(self) -> str:
        """Loads test input from .txt file for the day"""
        day_test_input_file = self.parent_dir / Path(f"test.txt")
        with io.open(day_test_input_file) as f:
            day_test_input = f.read() 
        return day_test_input

    def test(self, solution: callable, answer: int, should_crash: bool = True) -> None:
        """Tries solution on test input"""
        msg = f"Testing {solution.__name__}"
        print(f"{msg}\n{'-'*len(msg)}")
        guess = solution(self.test_input)
        result = f"Guess: {guess}\nAnswer: {answer}"
        if guess != answer and should_crash: raise AssertionError(result)
        print(result, "\n")
        return

    def get_full_input(self) -> str:
        """Loads input from .txt file for the day"""
        day_input_file = self.parent_dir / Path(f"input.txt")
        with io.open(day_input_file) as f:
            day_input = f.read()
        return day_input

    def solve(self, solution: callable) -> None:
        """Tries solution on full input"""
        msg = f"Solving {solution.__name__}"
        print(f"{msg}\n{'-'*len(msg)}")
        guess = solution(self.full_input)
        result = f"{self} Answer: {guess}"
        print(result, "\n")
        return