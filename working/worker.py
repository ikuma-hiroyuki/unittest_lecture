from datetime import datetime, timedelta


class Worker:
    """ 労働者 """
    SCHEDULED_WORKINGTIME = 8.0  # 所定労働時間

    def __init__(
            self,
            name: str,
            starting_time: datetime,
            finishing_time: datetime,
            break_time: timedelta,
            is_weekday: bool
    ):
        """
        :param name: 名前
        :param starting_time: 出勤時間
        :param finishing_time: 退勤時間
        :param break_time: 休憩時間
        :param is_weekday: 勤務日区分
        """

        self.name = name
        self.starting_time = starting_time
        self.finishing_time = finishing_time
        self.break_time = break_time
        self.is_weekday = is_weekday

        self.total_worktime = self._calc_total_worktime()  # 総労働時間
        self.scheduled_worktime = self._calc_scheduled_worktime()  # 平日所定内労働時間
        self.over_worktime = self._calc_overtime()  # 平日所定外時間
        self.holiday_worktime = self._calc_holiday_worktime()  # 休日労働時間

    def _calc_total_worktime(self) -> float:
        """
        総労働時間を計算する

        :return: 総労働時間 (時単位)
        """

        return (self.finishing_time - self.starting_time - self.break_time).seconds / 3600

    def _calc_scheduled_worktime(self) -> float:
        """
        平日所定内労働時間を計算する

        :return: 平日所定内労働時間 (時単位)
        """

        if self.is_weekday:
            overflow_time = self.total_worktime - self.SCHEDULED_WORKINGTIME
            if overflow_time > 0:
                return self.SCHEDULED_WORKINGTIME
            else:
                return self.total_worktime
        return 0.0

    def _calc_overtime(self) -> float:
        """
        平日所定外時間を計算する

        :return: 平日所定外時間 (時単位)
        """

        if self.is_weekday:
            overflow_time = self.total_worktime - self.SCHEDULED_WORKINGTIME
            if overflow_time > 0:
                return overflow_time
            else:
                return 0.0
        return 0.0

    def _calc_holiday_worktime(self) -> float:
        """
        休日労働時間を計算する

        :return: 休日労働時間 (時単位)
        """

        return self.total_worktime if not self.is_weekday else 0.0
