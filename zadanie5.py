kwota = int(input("Podaj kwotę: "))
typ = input("Wybierz walute :THB/BTC/BTN/MRO/ETH/USD: ")
typ2 = input("Na jaką walute chcesz przewalutować: THB/BTC/BTN/MRO/ETH/USD: ")

def waluta(kwota, typ, typ2):
    if typ=="THB":
        z = kwota*0.33
    elif typ =="BTC":
        z = kwota*37320
    elif typ =="BTN":
        z = kwota*0.14
    elif typ =="ETH":
        z = kwota*1416.12
    elif typ =="MRO":
        z = kwota*0.27
    elif typ =="USD":
        z = kwota*1

    if typ2=="THB":
        z = (z/0.33)
    elif typ2 =="BTC":
        z = (z/37320)
    elif typ2=="BTN":
        z = (z/0.14)
    elif typ2 =="MRO":
        z = (z/0.27)
    elif typ2 =="ETH":
        z = (z/1416.12)
    elif typ2 =="USD":
        z = z*1

    return z
print(waluta(kwota,typ,typ2))
