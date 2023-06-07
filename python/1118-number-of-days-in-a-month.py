import calendar


class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        days = [0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month != 2:
            return days[month]
        
        return 29 if calendar.isleap(year) else 28
