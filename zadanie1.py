def kalkulator(x):
    netto = x*0.68
    brutto = int(x)
    return netto

#ubezpieczenie emerytalne -19,52%
#ubezpieczenie rentowe -8%
#ubezpieczenie chorobowe -2,45%
#ubezpieczenie od wypadku -1,67%
#w przybliżeniu -32%

z = int(input("Podaj kwote netto: "))
print("To kwota którą dostaniesz na rękę:",kalkulator(z),"zł")
