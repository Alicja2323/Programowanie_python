    import json
    import random
    import warnings
    warnings.simplefilter('ignore', category=DeprecationWarning)
#import warnings usuwa nam problem powtarzalności pytań w quizie

    def ocena(punkty):
        if punkty < 2:
            return "niedostateczny"
        elif punkty < 4:
            return "dopuszczajacy"
        elif punkty < 6:
            return "dostateczny"
        elif punkty < 8:
            return "dobry"
        elif punkty < 9:
            return "bardzo dobry"
        else:
            return "celujacy"

    def quiz(plik_pytania):
        text = open(plik_pytania, "r").read()
        pytania = json.loads(text)
        punkty = 0
        pytania = random.sample(pytania.items(), 10) #Losujemy randomowo 10 pytań,które się nie powtarzają
        for pytanie, odp in pytania:
            print(pytanie)
            odpowiedz = input("TAK/NIE").upper() #.upper ma za zadanie odczytywać znaki z małej i z dużej litery
            if odpowiedz == odp:
                punkty += 1
        print(f"Uzyskales ocene: {ocena(punkty)}")

    if __name__ == "__main__":
        quiz("pytania.json")