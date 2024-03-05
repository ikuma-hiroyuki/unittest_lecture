from .worker import Worker


class Payroll:
    """給与計算"""

    def __init__(self, worker: Worker, hourly_pay: int):
        """
        :param worker: 労働者
        :param hourly_pay: 時給
        """
        self._worker = worker
        self._hourly_pay = hourly_pay

    @property
    def scheduled_salary(self):
        """平日所定内労働の給与"""
        return self._worker.scheduled_worktime.seconds / 3600 * self._hourly_pay

    @property
    def overtime_salary(self):
        """平日所定外労働の給与"""
        return self._worker.over_worktime.seconds / 3600 * self._hourly_pay * 1.25

    @property
    def holiday_salary(self):
        """休日労働の給与"""
        return self._worker.holiday_worktime.seconds / 3600 * self._hourly_pay * 1.35

    @property
    def total_salary(self):
        """給与合計"""
        return self.scheduled_salary + self.overtime_salary + self.holiday_salary