from pathlib import Path
from aoc2022.aoc2022 import Day

shapes = ["rock", "paper", "scissors"]

# (rock (0) + scissors (2) + 1) % 3
# (scissors (2) + scissors(2) + 1) % 3

def part1(day_in: str) -> int:
    """Calculate score from strategy guide"""
    rock, paper, scissors = 0, 1, 2
    opponent_shapes = {"A": rock, "B": paper, "C": scissors, }
    my_shapes = { "X": rock, "Y": paper, "Z": scissors, }
    shape_pts = {rock: 1, paper: 2, scissors: 3}
    draw, win, loss = 0, 1, 2
    outcome_pts = {loss: 0, draw: 3, win: 6}
    total_score = 0
    for round in day_in.splitlines():
        opponent_play, my_play = round.split(" ")
        opponent = opponent_shapes[opponent_play]
        me = my_shapes[my_play]
        # Modulo difference
        outcome = (me - opponent) % len(my_shapes)
        score = outcome_pts[outcome] + shape_pts[me]
        total_score += score
    return total_score

def part2(day_in: str) -> int:
    """Calculate score from strategy guide"""
    rock, paper, scissors = 0, 1, 2
    opponent_shapes = {"A": rock,"B": paper,"C": scissors,}
    draw, win, loss = 0, 1, 2
    outcomes = {"X": loss,"Y": draw,"Z": win,}
    shape_pts = {rock: 1, paper: 2, scissors: 3}
    outcome_pts = {loss: 0, draw: 3, win: 6}
    total_score = 0
    for round in day_in.splitlines():
        opponent_play, outcome = round.split(" ")
        opponent = opponent_shapes[opponent_play]
        outcome_num = outcomes[outcome]
        me = None
        if outcome_num == loss:
            me = (opponent - 1) % len(outcomes)
        elif outcome_num == win:
            me = (opponent + 1) % len(outcomes)
        elif outcome_num == draw:
            me = opponent
        score = outcome_pts[outcome_num] + shape_pts[me]
        total_score += score
    return total_score

if __name__ == "__main__":
    day02 = Day(2, Path("./day02"))

    day02.test(part1, answer=15)
    day02.solve(part1)
    
    day02.test(part2, answer=12)
    day02.solve(part2)