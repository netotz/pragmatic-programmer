from dataclasses import dataclass

from exercise4.instruction import Instruction


@dataclass
class InstructionsList:
    """
    List of instructions.
    """

    def __init__(self) -> None:
        self.__instructions: list[Instruction] = []

    def add(self, instruction: Instruction) -> None:
        """
        Adds an instruction.
        """
        self.__instructions.append(instruction)
