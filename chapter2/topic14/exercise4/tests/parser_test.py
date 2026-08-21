from pathlib import Path

import pytest

from exercise4.parser import parse_file, COMMANDS
from exercise4.instruction import Instruction

DATA_DIR = Path(__file__).parent / "data"


@pytest.mark.parametrize(
    ("filepath", "expected_instructions"),
    [
        (
            DATA_DIR / "test1.txt",
            [
                Instruction(
                    COMMANDS["D"],
                ),
                Instruction(
                    COMMANDS["U"],
                ),
            ],
        ),
    ],
)
def test_parser(filepath: str, expected_instructions: list[Instruction]):
    actual = parse_file(filepath)

    # requires overriding comparing method
    # assert actual == expected_instructions

    assert len(actual) == len(expected_instructions)

    for actual_inst, expected_inst in zip(actual, expected_instructions):
        assert (
            actual_inst.command.key == expected_inst.command.key
            and actual_inst.argument == expected_inst.argument
        )
