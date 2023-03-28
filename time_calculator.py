def add_time(start, duration, day=""):
    daysPassed = 0

    start_hour, start_minute = start.split(':')
    start_minute, start_time = start_minute.split()

    start_hour_int = int(start_hour)
    start_minute_int = int(start_minute)

    duration_hour, duration_minute = duration.split(':')

    duration_hour_int = int(duration_hour)
    duration_minutes_int = int(duration_minute)

    if start_time == 'PM' and start_hour_int != 12:
        start_hour_int += 12
    elif start_time == 'AM' and start_hour_int == 12:
        start_hour_int = 0

    new_hour = start_hour_int + duration_hour_int
    new_minutes = start_minute_int + duration_minutes_int
    if new_minutes >= 60:
        new_minutes -= 60
        new_hour += 1

    daysPassed += new_hour // 24
    new_hour -= 24 * daysPassed 

    time_of_day = checkIfPM(new_hour)
    new_minutes = add_zero(new_minutes)
    if new_hour > 12:
        new_hour -= 12
    if new_hour == 0:
        new_hour = 12
    new_time = "{}:{} {}{}{}".format(
        str(new_hour), new_minutes, time_of_day, daysOfTheWeek(day, daysPassed), daysPassedStr(daysPassed))

    return new_time


def daysOfTheWeek(day, daysPassed):
    daysInWeek = ["monday", "tuesday", "wednesday",
                        "thursday", "friday", "saturday", "sunday"]
    if day == "":
        return ""
    else:
        day_str = day.lower()
        indexOfDay = daysInWeek.index(day_str) + daysPassed
        if indexOfDay >= 7:
            indexOfDay -= (indexOfDay // 7) * 7
        return ", {}".format(daysInWeek[indexOfDay].capitalize())

def daysPassedStr(daysPassed):
    if daysPassed == 0:
        return ""
    elif daysPassed == 1:
        return " (next day)"
    elif daysPassed > 1:
        return " ({} days later)".format(daysPassed)


def checkIfPM(hour):
    if (hour >= 12):
        return "PM"
    else:
        return "AM"


def add_zero(num):
    if num < 10:
        return '0' + str(num)
    else:
        return str(num)
