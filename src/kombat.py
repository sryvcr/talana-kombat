from src.constants import (
    ARNALDOR,
    CHARACTER_ATTACKS,
    HITS,
    HIT_WORDS,
    MOVEMENTS,
    TONYN,
)


class KombatCharacter:
    def __init__(
        self,
        name: str,
        moves: list,
        hits: list,
    ) -> None:
        self.__energy = 6
        self.name = name
        self.moves = moves
        self.hits = hits

    @property
    def energy(self) -> int:
        return self.__energy

    @energy.setter
    def energy(self, character_energy: int) -> None:
        self.__energy = character_energy

    def get_moves_count(self) -> int:
        not_empty_moves = [move for move in self.moves if move]
        return len(not_empty_moves)


class Kombat:
    def __init__(self) -> None:
        data = self.get_kombat_data()
        self.player_1 = KombatCharacter(
            name=TONYN,
            moves=data["player1"]["movimientos"],
            hits=data["player1"]["golpes"],
        )
        self.player_2 = KombatCharacter(
            name=ARNALDOR,
            moves=data["player2"]["movimientos"],
            hits=data["player2"]["golpes"],
        )

    def get_kombat_data(self) -> dict:
        return {
            "player1": {
                "movimientos": ["D", "DSD", "S", "DSD", "SD"],
                "golpes": ["K", "P", "", "K", "P"],
            },
            "player2": {
                "movimientos": ["SA", "SA", "SA", "ASA", "SA"],
                "golpes": ["K", "", "K", "P", "P"],
            }
        }
