from pathlib import Path
from aoc2022.aoc2022 import Day

def get_crates(idx: int, reverse_crate_rows: list[list[str]]):
    """Find all the crate letters at a particular index, going bottom to top"""
    crates = list()
    for row in reverse_crate_rows:
        if row[idx].isalpha():
            crates.append(row[idx])
    return crates

def parse_crate_map(crates: str):
    # print(crates)
    crate_rows = crates.split("\n")
    # Parse crates (str -> list[str])
    positions = crate_rows[-1]
    crate_map = dict()
    for i, character in enumerate(positions):
        if character.isdigit():
            crate_map[int(character)] = get_crates(i, crate_rows[::-1])
    return crate_map

def print_crate_map(crate_map: dict[int, list[str]]) -> None:
    print()
    for pos, crates in crate_map.items():
        print(f"{pos} {' '.join([f'[{crate}]' for crate in crates])}")
    print()
    return

def exec_crate_command(crate_map: dict[int, list[str]], num_crates: int, pos_start: int, pos_end: int):
    # Grab crates ONE AT A TIME
    # print(f"\tGrabbing {num_crates} crates from {pos_start}: ")
    for _ in range(num_crates):
        moved_crates = crate_map.get(pos_start)[-1]
        crate_map[pos_start] = crate_map.get(pos_start)[:-1]
        crate_map[pos_end] = [*crate_map.get(pos_end), *moved_crates]
    # print(f"\tAdded crates to {pos_end}")
    # print()
    return crate_map



def exec_crate_commands(command_set: str, crate_map: dict[int, list[str]], multi=False):
    commands = command_set.split("\n")
    for command in commands:
        match command.split(" "):
            case ["move", num_crates, "from", pos_start, "to", pos_end]:
                if multi:
                    crate_map = exec_multi_crate_command(crate_map, int(num_crates), int(pos_start), int(pos_end))
                else:
                    crate_map = exec_crate_command(crate_map, int(num_crates), int(pos_start), int(pos_end))
                # print_crate_map(crate_map)
    return crate_map

def get_top_stack(crate_map: dict[int, list[str]]):
    return ''.join([stack[-1] for stack in crate_map.values()])

def part1(day_in: str) -> int:
    # Separate crates from commands
    crates, command_set = day_in.split("\n\n")
    # Get crate map
    crate_map = parse_crate_map(crates)
    # print(crate_map)
    # Run commands
    resulting_crate_map = exec_crate_commands(command_set, crate_map)
    top_crates = get_top_stack(resulting_crate_map)
    return top_crates

def exec_multi_crate_command(crate_map: dict[int, list[str]], num_crates: int, pos_start: int, pos_end: int):
    # Grab crates ONE AT A TIME
    # print(f"\tGrabbing {num_crates} crates from {pos_start}: ")
    moved_crates = crate_map.get(pos_start)[-num_crates:]
    crate_map[pos_start] = crate_map.get(pos_start)[:-num_crates]
    crate_map[pos_end] = [*crate_map.get(pos_end), *moved_crates]
    # print(f"\tAdded crates to {pos_end}")
    # print()
    return crate_map

def part2(day_in: str) -> int:
    # Separate crates from commands
    crates, command_set = day_in.split("\n\n")
    # Get crate map
    crate_map = parse_crate_map(crates)
    # print(crate_map)
    # Run commands
    resulting_crate_map = exec_crate_commands(command_set, crate_map, multi=True)
    top_crates = get_top_stack(resulting_crate_map)
    return top_crates

if __name__ == "__main__":
    day05 = Day(5, Path("./day05"))

    day05.test(part1, answer="CMZ")
    day05.solve(part1)
    
    day05.test(part2, answer="MCD")
    day05.solve(part2)