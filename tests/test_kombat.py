import pytest
from unittest import mock

from src.constants import ARNALDOR, TONYN
from src.kombat import KombatCharacter, Kombat
from tests.recipes import kombat_1_data, kombat_2_data


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
        ],
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


class TestKombat:
    def setup_method(self):
        mock_get_kombat_data = mock.patch(
            "src.kombat.Kombat.get_kombat_data", return_value=kombat_2_data
        )
        mock_get_kombat_data.start()

        self.kombat = Kombat()

    def test_get_starting_player(self):
        first_player = self.kombat.get_starting_player()

        assert first_player.name == TONYN

    @pytest.mark.parametrize(
        ["player_1_energy", "player_2_energy", "is_there_a_winner", "win_message"],
        [
            (0, 0, True, "La pelea termina en un empate\n"),
            (0, 3, True, f"{ARNALDOR} gana la pelea y aún le quedan 3 de energía\n"),
            (1, 0, True, f"{TONYN} gana la pelea y aún le quedan 1 de energía\n"),
            (1, 2, False, ""),
        ],
    )
    def test_is_there_a_winner(
        self, player_1_energy, player_2_energy, is_there_a_winner, win_message, capfd
    ):
        self.kombat.player_1.energy = player_1_energy
        self.kombat.player_2.energy = player_2_energy

        result = self.kombat.is_there_a_winner()
        out, _ = capfd.readouterr()

        assert out == win_message
        assert result == is_there_a_winner

    def test_start(self, capfd):
        fight_comments = (
            f"{TONYN} da una patada\n"
            f"{ARNALDOR} avanza y da un puño\n"
            f"{TONYN} usa un Taladoken\n"
            f"{ARNALDOR} da una patada\n"
            f"{TONYN} avanza y da una patada\n"
            f"{ARNALDOR} avanza y da una patada\n"
            f"{TONYN} usa un Taladoken\n"
            f"{TONYN} gana la pelea y aún le quedan 3 de energía\n"
        )
        self.kombat.start()
        out, _ = capfd.readouterr()

        assert out == fight_comments
        assert self.kombat.player_1.energy == 3
        assert self.kombat.player_2.energy == -2
