print("Projekt 1: Textový anlyzátor")
print("Autor: Tomáš Hensperger")

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

username = input("Username: ")
password = input("Password: ")

users = {"bob" : "123", "ann" : "pass123", "mike" : "password123", "liz" : "pass123"}

texts_max = len(TEXTS)
choice = None
choice_wordlist = []

if password in users[username]: #kontrola uzivatele a spravneho hesla
    print("-" * 40)
    print("Welcome to the app, " + username)
    print("We have " + str(texts_max) + " texts to be analyzed.")
    print("-" * 40)
    choice = input("Enter a number btw. 1 and " + str(texts_max) + " to select: ")
    if not choice.isdigit():
        print("Invalid input, terminating the program...")
        exit()
    elif int(choice) > texts_max:
        print("Selected text does not exist (out of range). Terminating the program...")
        exit()
    else:
        
        print("-" * 40)
        print(TEXTS[int(choice)-1])
        print("-" * 40)
        choice_wordlist = TEXTS[int(choice)-1].split()
        slova = list(text.split())
        print(slova)


        pocet_slov = 0
        nazvy_slov = 0
        velke_pismena = 0
        male_pismena = 0
        pocet_cisel = 0
        soucet_cisel = 0

        for slovo in slova:
            pocet_slov += 1 
            if slovo.istitle():
                nazvy += 1
            elif slovo.isupper():
                velke += 1
            elif slovo.islower():
                male += 1
            elif slovo.isdigit():
                pocet_cisel += 1
                soucet_cisel += int(slovo)



        print("---" * 40)
        print(f"pocet slov: {pocet_slov}")
        print(f"pocet slov zacinajicich velkym pismenenm: {nazvy}")
        print(f"pocet velkych: {velke}")
        print(f"pocet malych: {male}")
        print(f"pocet cisel: {pocet_cisel}")
        print(f"soucet: {soucet}")

else:
    print("Unregistered user, terminating the program...")
    exit()

