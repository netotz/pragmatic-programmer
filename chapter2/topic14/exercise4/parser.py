from .command import Command
from .instruction import Instruction

COMMANDS = {
    "D": Command("D", "pen down", False),
    "U": Command("U", "pen up", False),
    "P": Command("P", "select pen", True),
    "W": Command("W", "draw west", True),
    "E": Command("E", "draw east", True),
    "N": Command("N", "draw north", True),
    "S": Command("S", "draw south", True),
    # ...
}
"""
Dictionary of valid commands.
"""


def try_validate_argument(string: str) -> int | None:
    """
    Tries converting the raw argument into an integer.
    If the input was invalid, returns `None`.
    """
    try:
        return int(string)
    except ValueError:
        return None


def parse_file(filepath: str) -> list[Instruction]:
    """
    Tries to open the received `filepath` and parses its content
    into a sequence of instructions.
    """
    instructions: list[Instruction] = []

    with open(filepath, "r") as file:
        for i, line in enumerate(file):
            stripped = line.strip()
            split = stripped.split(" ")

            # skip/allow empty lines
            if len(split) == 0:
                continue

            # possible command
            command_key = split[0]

            # skip comment lines
            if command_key.startswith("#"):
                continue

            if command_key not in COMMANDS:
                # handle invalid command
                continue

            command = COMMANDS[command_key]

            # if command doesn't need argument,
            # create and add instruction
            if not command.does_require_arg:
                instruction = Instruction(command)
                instructions.append(instruction)

                continue

            # if there's no argument
            if len(split) < 2:
                # handle error
                continue

            raw_argument = split[1]
            argument = try_validate_argument(raw_argument)
            # if invalid argument
            if argument is None:
                # handle error
                continue

            instruction = Instruction(command, argument)
            instructions.append(instruction)

    return instructions
