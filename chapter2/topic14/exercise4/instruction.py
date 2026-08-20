from .command import Command


class Instruction:
    """
    Pair of a command with its argument, if it requires one.
    """

    def __init__(self, command: Command, argument: int | None = None) -> None:
        # if command requires and argument but it's not provided
        if command.does_require_arg and argument is None:
            raise ValueError(
                f"Command {command} requires an argument, but none was given."
            )

        self.command = command
        self.argument = argument
