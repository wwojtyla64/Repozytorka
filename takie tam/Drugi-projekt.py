##              RANDOMOWE WYCZYTANIE WARTOSCI Z LISTY
##import random
##slownik=['jeden','dwa','trzy','cztery','piec','szesc']
##nowy_slownik=[]
##
##while slownik != []:
##    index=random.randrange(len(slownik))
##    nowy_slownik.append(slownik[index])
####    del slownik[index]
##    slownik.remove(slownik[index])
##print(nowy_slownik)

##def urodziny(name ="Janusz", age = 17):
##    print("WITAJ ",name,", masz już ",age," lat!")
##
##urodziny(age=9,name='Krzysztof')

##             ZGADYWANIE NUMERU(GRA)
##import random
##
##liczba=random.randint(1,100)
##your_number=0
##def ask_number():
##    your_number=int(input("podaj liczbę z przedziału [1-100] : "))
##    while your_number not in range(1,100):
##            your_number=int(input("podaj liczbę z przedziału [1-100] : "))
##    return your_number
##
##while your_number != liczba:
##    your_number=ask_number()
##    if your_number>liczba:
##        print("za duża")
##    elif your_number<liczba:
##        print("za mala")
##    else:
##        print("GRATULACJE WYGRAŁES! Ta liczba to %d " % liczba)
    
