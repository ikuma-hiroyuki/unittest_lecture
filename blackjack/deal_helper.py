import os
from enum import Enum


class ScoreRules(Enum):
    """スコア計算に関するルールを表す列挙型"""
    BLACK_JACK = 21
    DEALER_MIN = 17


class Odds(Enum):
    """掛け金分配率を表す列挙型"""
    NATURAL_BLACK_JACK = 1.5
    WIN = 1
    DRAW = 0
    LOSE = -1


def ask_stand():
    """スタンドするかどうか尋ねる"""
    return bool(input(
        'スタンドする場合は何か入力してエンターキーを押してください。何も入力せずエンターキーを押すとヒットします。:\n'))


def ask_user_replay_decision():
    """ユーザーに再戦するかどうか尋ねる"""
    return not bool(input('終了する場合は何か入力してエンターキーを押してください: '))


def ask_bets(current_money):
    """
    掛け金をユーザーに尋ねる

    掛け金は1以上、かつ所持金以下の整数でなければならない
    :param: current_money: 現在の所持金
    :return: 掛け金
    """

    minimum_bet_amount = 1
    while True:
        input_value = input(f'掛け金を入力してください。現在の所持金 {current_money}: ')
        if not input_value.isdigit():
            print('掛け金は整数で入力してください。')
            continue
        bet_amount = int(input_value)
        if bet_amount < minimum_bet_amount or bet_amount > current_money:
            print(f'掛け金は{minimum_bet_amount}円以上、かつ所持金以下の整数で入力してください。')
            continue
        return bet_amount


def clear_terminal():
    """ターミナルをクリアする"""
    os.system('cls' if os.name == 'nt' else 'clear')
