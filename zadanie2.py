def koszt(brutto):
    renta = brutto*0.065
    emerytura = brutto*0.0976
    wypadek = brutto*0.0167
    dhsp = brutto*0.01
    return brutto + renta + emerytura + wypadek + dhsp
brutto = float(input("Podaj kwote: "))
print(koszt(brutto) ,"tyle po dodaniu podatków wydał na ciebie twój pracodawca")