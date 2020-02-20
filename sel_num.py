def aff(day, num):
    if day == 'Monday':
        return num == 12
    if day == "Tuesday":
        return num > 95
    if day == "Wednesday":
        return num == 0
    if day == "Friday":
        return num % 2 == 0
    if day == "Saturday":
        return num == 56
    if day == "Sunday":
        return abs(num) == 666
    return False


print(aff("Monday", 12))
