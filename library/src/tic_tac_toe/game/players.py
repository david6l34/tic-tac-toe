import abc
import random
import time

from tic_tac_toe.logic.exceptions import InvalidMove
from tic_tac_toe.logic.models import Mark, GameState, Move


class Player:
    def __init__(self, mark: Mark) -> None:
        self.mark = mark

    def make_move(self, game_state: GameState) -> GameState:
        if self.mark is not game_state.current_mark:
            raise InvalidMove("It's the other player's turn")
        if not (move := self.get_move(game_state)):
            raise InvalidMove("No more possible moves")
        return move.after_state

    @abc.abstractmethod
    def get_move(self, game_state: GameState) -> Move | None:
        """Return the current player's move in the given game state."""

class ComputerPlayer(Player):
    def __init__(self, mark: Mark, delay_seconds: float = 0.25):
        super().__init__(mark)
        self.delay_seconds = delay_seconds

    def get_move(self, game_state: GameState) -> Move | None:
        time.sleep(self.delay_seconds)
        return self.get_computer_move(game_state)

    @abc.abstractmethod
    def get_computer_move(self, game_state: GameState) -> Move | None:
        """Return the computer's move in the given game state."""

class RandomComputerPlayer(ComputerPlayer):
    def get_computer_move(self, game_state: GameState) -> Move | None:
        if game_state.possible_moves:
            return random.choice(game_state.possible_moves)
        return None




