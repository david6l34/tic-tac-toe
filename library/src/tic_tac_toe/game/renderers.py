import abc

from tic_tac_toe.logic.models import GameState


class Renderer:
    @abc.abstractmethod
    def render(self, game_state: GameState) -> None:
        """Render the current game state."""


