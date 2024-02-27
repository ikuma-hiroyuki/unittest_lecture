from unittest import TestCase
from janken.hands import rock, paper, scissors

from janken.player import User, CPU
from janken.referee import Referee


class TestReferee(TestCase):
    """ Referee のテスト """

    @classmethod
    def setUpClass(cls):
        cls.user = User()
        cls.cpu = CPU()
        cls.referee = Referee()

    def test_user_win_rock_vs_scissors(self):
        """ ユーザーがグー、CPUがチョキでユーザーが勝つケース """
        self.user.hand = rock
        self.cpu.hand = scissors
        self.referee.evaluate_judge(self.user, self.cpu)
        result = self.referee._is_user_win(self.user.hand, self.cpu.hand)
        self.assertTrue(result)

    def test_user_win_scissors_vs_paper(self):
        """ ユーザーがチョキ、CPUがパーでユーザーが勝つケース """
        self.user.hand = scissors
        self.cpu.hand = paper
        self.referee.evaluate_judge(self.user, self.cpu)
        result = self.referee._is_user_win(self.user.hand, self.cpu.hand)
        self.assertTrue(result)

    def test_user_win_paper_vs_rock(self):
        """ ユーザーがパー、CPUがグーでユーザーが勝つケース """
        self.user.hand = paper
        self.cpu.hand = rock
        self.referee.evaluate_judge(self.user, self.cpu)
        result = self.referee._is_user_win(self.user.hand, self.cpu.hand)
        self.assertTrue(result)

    def test_judge_message_win(self):
        """ 勝利メッセージのテスト """
        self.user.hand = paper
        self.cpu.hand = rock
        self.referee.evaluate_judge(self.user, self.cpu)
        self.assertEqual(self.referee.judgment_result, "勝ち！")

    def test_judge_message_lose(self):
        """ 敗北メッセージのテスト """
        self.user.hand = rock
        self.cpu.hand = paper
        self.referee.evaluate_judge(self.user, self.cpu)
        self.assertEqual(self.referee.judgment_result, "負け")

    def test_judge_message_draw(self):
        """ 引き分けメッセージのテスト """
        self.user.hand = rock
        self.cpu.hand = rock
        self.referee.evaluate_judge(self.user, self.cpu)
        self.assertEqual(self.referee.judgment_result, "あいこ")