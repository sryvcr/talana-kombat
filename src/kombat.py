from src.constants import (
    ARNALDOR,
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
