import enum
import re
from dataclasses import dataclass


class Mark(str, enum.Enum):
    CROSS = 'X'
    NAUGHT = 'O'

    @property
    def other(self) -> 'Mark':
        return Mark.CROSS if self is Mark.NAUGHT else Mark.NAUGHT

@dataclass(frozen=True)
class Grid:
    cells: str = " " * 9

    def __post_init__(self) -> None:
        if not re.match(r"^[\sXO]{9}$", self.cells):
            raise ValueError("Must contain 9 cells of: X, O, or space")