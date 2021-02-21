class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        return abs(self.f(date1) - self.f(date2))
    
    def f(self, date):
        year, month, day = map(int, date.split('-'))
        days = 365 * year - 1 - 1971
        if year > 1971:
            days += sum(map(self.is_leap, range(1971, year)))
        days += 30 * month
        if month > 2:
            if self.is_leap(year) == 1:
                days -= 1
            else:
                days -= 2
        for i in [1,3,5,7,8,10,12]:
            if month > i:
                days += 1
            else: 
                break
        return days + day
    
    def is_leap(self, x):
        return 1 if (x % 4 == 0 and x % 100 > 0) or ( x % 400 == 0) else 0
