import pytest

from src.constants import ARNALDOR, TONYN
from src.kombat import KombatCharacter
from tests.recipes import kombat_1_data


class TestKombatCharacter:
    def setup_method(self):
        self.player_1 = KombatCharacter(
            name=TONYN,
            moves=kombat_1_data["player1"]["movimientos"],
            hits=kombat_1_data["player1"]["golpes"],
        )

        self.player_2 = KombatCharacter(
            name=ARNALDOR,
            moves=kombat_1_data["player2"]["movimientos"],
            hits=kombat_1_data["player2"]["golpes"],
        )

    def test_get_energy(self):
        assert self.player_1.energy == 6
        assert self.player_2.energy == 6

    def test_set_energy(self):
        self.player_1.energy -= 6
        self.player_2.energy -= 2

        assert self.player_1.energy == 0
        assert self.player_2.energy == 4

    @pytest.mark.parametrize(
        ["index", "message", "remaining_energy"],
        [
            (0, "Tonyn avanza y da una patada\n", 5),
            (1, "Tonyn usa un Taladoken\n", 3),
            (2, "Tonyn avanza\n", 6),
            (4, "Tonyn avanza y da un puño\n", 5),
        ]
    )
    def test_execute_action_movement_and_hit(
        self, index, message, remaining_energy, capfd
    ):
        self.player_1.execute_action(
            movement=self.player_1.moves[index],
            hit=self.player_1.hits[index],
            oponent=self.player_2,
        )

        out, _ = capfd.readouterr()
        assert out == message
        assert self.player_2.energy == remaining_energy

    def test_get_moves_count(self):
        assert self.player_1.get_moves_count() == 5
        assert self.player_2.get_moves_count() == 5

    def test_get_hits_count(self):
        assert self.player_1.get_hits_count() == 4
        assert self.player_2.get_hits_count() == 4

    def test_get_combos_count(self):
        assert self.player_1.get_combos_count() == 4
        assert self.player_2.get_combos_count() == 4
