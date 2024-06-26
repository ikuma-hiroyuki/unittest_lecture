from unittest import TestCase

from janken.hands import rock, paper, scissors
from janken.player import User, CPU
from janken.referee import Referee


class TestReferee(TestCase):
    """ Referee のテスト """

    def setUp(self):
        self.user = User()
        self.cpu = CPU()
        self.referee = Referee()

    def test_user_win_rock_vs_scissors(self):
        """ ユーザーがグー、CPUがチョキでユーザーが勝つケース """
        self.user.hand = rock
        self.cpu.hand = scissors
        result = self.referee._is_user_win(self.user.hand, self.cpu.hand)
        self.assertTrue(result)

    def test_user_win_scissors_vs_paper(self):
        """ ユーザーがチョキ、CPUがパーでユーザーが勝つケース """
        self.user.hand = scissors
        self.cpu.hand = paper
        result = self.referee._is_user_win(self.user.hand, self.cpu.hand)
        self.assertTrue(result)

    def test_user_win_paper_vs_rock(self):
        """ ユーザーがパー、CPUがグーでユーザーが勝つケース """
        self.user.hand = paper
        self.cpu.hand = rock
        result = self.referee._is_user_win(self.user.hand, self.cpu.hand)
        self.assertTrue(result)

    def test_user_lose_rock_vs_paper(self):
        """ ユーザーがグー、CPUがパーでユーザーが負けるケース """
        self.user.hand = rock
        self.cpu.hand = paper
        result = self.referee._is_user_win(self.user.hand, self.cpu.hand)
        self.assertFalse(result)

    def test_user_lose_scissors_vs_rock(self):
        """ ユーザーがチョキ、CPUがグーでユーザーが負けるケース """
        self.user.hand = scissors
        self.cpu.hand = rock
        result = self.referee._is_user_win(self.user.hand, self.cpu.hand)
        self.assertFalse(result)

    def test_user_lose_paper_vs_scissors(self):
        """ ユーザーがパー、CPUがチョキでユーザーが負けるケース """
        self.user.hand = paper
        self.cpu.hand = scissors
        result = self.referee._is_user_win(self.user.hand, self.cpu.hand)
        self.assertFalse(result)

    def test_draw_rock_vs_rock(self):
        """ ユーザーがグー、CPUもグーで引き分け """
        self.user.hand = rock
        self.cpu.hand = rock
        self.referee.evaluate_judge(self.user, self.cpu)
        self.assertFalse(self.referee.game_decided)

    def test_draw_scissors_vs_scissors(self):
        """ ユーザーがチョキ、CPUもチョキで引き分け """
        self.user.hand = scissors
        self.cpu.hand = scissors
        self.referee.evaluate_judge(self.user, self.cpu)
        self.assertFalse(self.referee.game_decided)

    def test_draw_paper_vs_paper(self):
        """ ユーザーがパー、CPUもパーで引き分け """
        self.user.hand = paper
        self.cpu.hand = paper
        self.referee.evaluate_judge(self.user, self.cpu)
        self.assertFalse(self.referee.game_decided)

    def test_game_decided_user_win(self):
        """ ユーザーが勝つケース """
        self.user.hand = rock
        self.cpu.hand = scissors
        self.referee.evaluate_judge(self.user, self.cpu)
        self.assertTrue(self.referee.game_decided)

    def test_game_decided_user_lose(self):
        """ ユーザーが負けるケース """
        self.user.hand = rock
        self.cpu.hand = paper
        self.referee.evaluate_judge(self.user, self.cpu)
        self.assertTrue(self.referee.game_decided)

    def test_judge_message_win(self):
        """ ユーザーが勝った場合のメッセージ """
        self.user.hand = rock
        self.cpu.hand = scissors
        self.referee.evaluate_judge(self.user, self.cpu)
        self.assertEqual(self.referee.judgment_result, "勝ち！")

    def test_judge_message_lose(self):
        """ ユーザーが負けた場合のメッセージ """
        self.user.hand = rock
        self.cpu.hand = paper
        self.referee.evaluate_judge(self.user, self.cpu)
        self.assertEqual(self.referee.judgment_result, "負け")

    def test_judge_message_draw(self):
        """ 引き分けのメッセージ """
        self.user.hand = rock
        self.cpu.hand = rock
        self.referee.evaluate_judge(self.user, self.cpu)
        self.assertEqual(self.referee.judgment_result, "あいこ")
