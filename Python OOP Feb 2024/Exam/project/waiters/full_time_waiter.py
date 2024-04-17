from project.waiters.base_waiter import BaseWaiter


class FullTimeWaiter(BaseWaiter):
    HOURLY_PAYMENT = 15.0

    def __init__(self, name: str, hours_worked: int):
        super().__init__(name, hours_worked)

    def calculate_earnings(self):
        earnings = self.hours_worked * self.HOURLY_PAYMENT
        return earnings

    def report_shift(self):
        return f"{self.name} worked a full-time shift of {self.hours_worked} hours."
