"""RPS WITHOUT if-statements

https://medium.com/@jp.mfichtl/rock-paper-scissors-lizard-spock-or-why-math-is-awesome-for-coding-405dabe30f4

"""

from itertools import product 

shapes = ["rock", "paper", "scissors"]
shape_idx = [i for i in range(len(shapes))]
rock, paper, scissors = shape_idx

# draw = -1

key = {i:shape for i, shape in zip(shape_idx, shapes)}
print(key)

def winner(l_shape: int, r_shape: int, key: dict):
    win_eq = (l_shape - r_shape) % len(key)
    return key[win_eq]


draw = 0
win = 1
loss = 2

outcome = {
    0: "draw",
    1: "win",
    2: "loss",
}

answers = {
    (rock, rock): rock,
    (rock, paper): paper,
    (rock, scissors): rock,

    (paper, paper): paper,
    (paper, rock): paper,
    (paper, scissors): scissors,

    (scissors, scissors): scissors,
    (scissors, paper): scissors,
    (scissors, rock): rock,
}

answer_outcomes = {
    (rock, rock): draw,
    (rock, paper): loss,
    (rock, scissors): win,

    (paper, paper): draw,
    (paper, rock): win,
    (paper, scissors): loss,

    (scissors, scissors): draw,
    (scissors, paper): win,
    (scissors, rock): loss,
}

if __name__ == "__main__":
    shapes = [rock, paper, scissors]
    combinations = product(shapes, shapes)
    for combo in combinations:
        left, right = combo
        result = winner(left, right, outcome)
        answer = outcome[answer_outcomes[combo]]
        indicator = "<-- WRONG" if result != answer else ""
        
        print(f"winner({key[left]}, {key[right]}) = {result} {indicator}")