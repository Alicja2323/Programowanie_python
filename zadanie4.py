def producencioszuści(x):
    y = int(input("Podaj pojemność dysku w gigabajtach:"))
    y = y*1000000000
    return round(y/1024/1024/1024,2)
print(producencioszuści(2),"tyle naprawdę ma twój dysk gb ")