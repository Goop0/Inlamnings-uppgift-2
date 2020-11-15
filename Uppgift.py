while True:
    startvärde = int(input('skriv ett start värde '))
    if startvärde <=0:
          
        print('skriv ett tal som inte är negativt eller 0')
        break
    elif startvärde >0:
        värde = startvärde
        while startvärde <1000000:
            startvärde * 2
            dagar = startvärde/värde
            dagar=int(dagar)
        print(f'det tar {dagar} dagar')