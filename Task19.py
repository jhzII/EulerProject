# Дана следующая информация (однако, вы можете проверить ее самостоятельно):
# 1 января 1900 года - понедельник.
# В апреле, июне, сентябре и ноябре 30 дней.
# В феврале 28 дней, в високосный год - 29.
# В остальных месяцах по 31 дню.
# Високосный год - любой год, делящийся нацело на 4, однако последний год века (ХХ00)
#   является високосным в том и только том случае, если делится на 400.
# Сколько воскресений выпадает на первое число месяца в двадцатом веке (с 1 января 1901 года до 31 декабря 2000 года)?


class DDate:
    weekday = 1
    day = 1
    month = 1
    year = 1900

    def next_month(self):
        # меняем день недели
        if self.month in [4, 6, 9, 11]:
            self.set_weekday_before(30)
        elif self.month == 2:
            self.set_weekday_before(29 if self.leap_year() else 28)
        else:
            self.set_weekday_before(31)

        if self.month == 12:
            self.year += 1
            self.month = 1
        else:
            self.month += 1

    def next_year(self):
        self.set_weekday_before(366 if self.leap_year() else 365)
        self.year += 1

    def set_weekday_before(self, days):
        self.weekday = (self.weekday + days) % 7

    def leap_year(self) -> bool:
        return self.year % 400 == 0 if self.year % 100 == 0 else self.year % 4 == 0


def sunday_counter():
    date = DDate()
    date.next_year()    # 1901
    quantity = 0

    while date.year < 2001:
        if date.weekday == 0:
            quantity += 1
        date.next_month()

    return quantity


if __name__ == '__main__':
    print(sunday_counter())
