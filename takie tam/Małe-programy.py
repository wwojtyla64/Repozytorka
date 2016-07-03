#                   WYPISYWANIE LICZB OD-DO-CO ILE
##pocz = int(input("Podaj poczatek: "))
##kon = int(input("Podaj koniec: "))
##co_ile = int(input("Podaj różnice miedzye elementami : "))
##
##for i in range(pocz,kon,co_ile):
##    print(i)

#          ODWRACANIE WPROWADZONEGO SLOWA(CZY PALINDROM?)
##message=input("Nanpisz jakiś komunikat : ")
##reverse_message=message[::-1]
##print("Odwrócony komunikat to: ",reverse_message)
##if message==reverse_message:
##    print("Palindrom!")
##else:
##    print("Nie jest palindromem...:(")

##                  TWORZENIE ANAGRAMU SŁOWA
##import random
##quest = input("Wpisz jakieś słowo: ")
##anagram = ""
##
##while quest != "":
##    index=random.randrange(len(quest))
##    anagram+=quest[index]
##    quest=quest[:index]+quest[index+1:]
##
##print("Anagram slowa %s to jest: " % quest ,anagram)
##input("Wciśnij ENTER aby zakończyć...")
#               SZUBIENICA_MOJA
##import random
##
##words = "boisko mieszkanie szkoła biedronka balkon"
##words=words.split()
##choice_word = random.choice(words)
##print("Wybrane słowo posiada %d liter !" % len(choice_word))
##
##szubienica=list()
##print("Słowo: ",end=" ")
##for i in range(len(choice_word)):
##    szubienica.append("_")
##    
##print(szubienica)
##
##index=0
##for i in range(5):
##    char=input("Podaj litere: ")
##    while len(char)!= 1:
##        char=input("Podaj (jedną!) litere: ")
##        
##    licznikindex=0
##    if char in choice_word:
##        for j in choice_word:
##            if char==j:
##                szubienica[licznikindex] = char
##                licznikindex+=1
##            else:
##                licznikindex+=1
##        print(szubienica)            
##
##haslo=input("Podaj hasło: ")
##if choice_word==haslo:
##    print("GRATULACJE!")
##else:
##    print("niestety nie...")
##
##input("Wciśnij ENTER aby zakończyć...")






