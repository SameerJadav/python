def main():
    answer = input("What time is it? ")
    time = convert(answer)
    if time >= 7 and time <= 8:
        print("breakfast time")
    if time >= 12 and time <= 13:
        print("lunch time")
    if time >= 18 and time <= 19:
        print("dinner time")


def convert(time):
    #split the time in hours and minutes
    hours, minutes = time.split(":")
    _minutes = float(minutes) / 60
    return float(hours) + _minutes
    #time will be returned like 7.5, it won't be visible in terminal window


if __name__ == "__main__":
    main()