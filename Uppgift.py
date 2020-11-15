while True:
    startvalue = float(input('write a start value '))
    if startvalue <=0:
        print('enter a number that is not <=0')
        break
    elif startvalue >0:
        value = startvalue
        days = 0
        while value <1000000:
            days += 1
            value *= 2
            print(value)
        print(f'it takes {days} days')
        break