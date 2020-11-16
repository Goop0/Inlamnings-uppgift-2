while True: #den här koden räknar ut hur många job dagar det tar för att få 1000 000 kr om din dags lön dubblas varje gång
    startvalue = float(input('write a start value '))
    if startvalue <=0: #om värdet är mindre än 0 så kommer den att be dig att skriva något som inte är mindre eller lika med 0
        print('enter a number that is not <=0')
        break
    elif startvalue >0:
        value = startvalue
        days = 0
        while value <1000000:#medans value är mindre än 1000 000 så körs koden under
            days += 1 #räknar varje gång det gångras med en dag
            value *= 2 #gångrar värdet med 2 
            print(value)#vissar varje värde tills det blir >1000 000
        print(f'it takes {days} days') #den här koden säger hur många dagar det tar tills man får >1000 000
        