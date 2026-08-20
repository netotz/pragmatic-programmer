from dataclasses import dataclass


@dataclass
class Command:
    """
    A command of the domain language, identified by `key`,
    e.g. `D` for the "pen down" command.
    """

    key: str
    name: str
    does_require_arg: bool
