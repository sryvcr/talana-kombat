import json

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

    def get_hits_count(self) -> int:
        not_empty_hits = [hit for hit in self.hits if hit]
        return len(not_empty_hits)

    def get_combos_count(self) -> int:
        count = 0
        max_action = max([self.moves, self.hits], key=len)
        for index in range(len(max_action)):
            move = self.moves[index]
            hit = self.hits[index]
            if move and hit:
                count += 1

        return count

    def execute_action(
        self, movement: str, hit: str, oponent: "KombatCharacter"
    ) -> None:
        hit_energy = 0
        action_comment = ""

        if self.name in CHARACTER_ATTACKS.keys():
            action_comment += f"{self.name}"
            action_key = (movement, hit)
            if action_key in CHARACTER_ATTACKS[self.name]:
                action, hit_energy = CHARACTER_ATTACKS[self.name][action_key]
                action_comment += f" usa un {action}"
            else:
                if movement in MOVEMENTS:
                    action_comment += " avanza"
                if hit in HITS:
                    action_comment += f" y da {HIT_WORDS[hit]}"
                    hit_energy = 1

        oponent.energy -= hit_energy

        print(action_comment)


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
        print("Ingresa los valores del juego en formato JSON:")
        kombat_str = input()
        json_data = json.loads(kombat_str)
        return json_data

    def get_starting_player(self) -> KombatCharacter:
        player_1_combos = self.player_1.get_combos_count()
        player_1_moves = self.player_1.get_moves_count()
        player_1_hits = self.player_1.get_hits_count()

        player_2_combos = self.player_2.get_combos_count()
        player_2_moves = self.player_2.get_moves_count()
        player_2_hits = self.player_2.get_hits_count()

        if (
            player_1_combos > player_2_combos
            or player_1_moves > player_2_moves
            or player_1_hits > player_2_hits
        ):
            return self.player_2

        return self.player_1

    def is_there_a_winner(self) -> bool:
        if self.player_1.energy <= 0 or self.player_2.energy <= 0:
            if self.player_1.energy == self.player_2.energy:
                print("La pelea termina en un empate")
            elif self.player_1.energy > self.player_2.energy:
                print(
                    f"{self.player_1.name} gana la pelea y aún le quedan {self.player_1.energy} de energía"
                )
            elif self.player_2.energy > self.player_1.energy:
                print(
                    f"{self.player_2.name} gana la pelea y aún le quedan {self.player_2.energy} de energía"
                )
            return True

        return False

    def start(self) -> None:
        first_player = self.get_starting_player()
        second_player = self.player_1 if first_player != self.player_1 else self.player_2

        max_turns = max([self.player_1.moves, self.player_2.moves], key=len)

        for i in range(len(max_turns)):
            try:
                first_player.execute_action(
                    movement=first_player.moves[i],
                    hit=first_player.hits[i],
                    oponent=second_player,
                )
            except IndexError:
                pass
            if self.is_there_a_winner():
                break

            try:
                second_player.execute_action(
                    movement=second_player.moves[i],
                    hit=second_player.hits[i],
                    oponent=first_player,
                )
            except IndexError:
                pass
            if self.is_there_a_winner():
                break
