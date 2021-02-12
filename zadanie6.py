def stanwody(x):
    F = 32 + x *1.8
    if(F<33):
        print("Woda zamarza")
    elif(F>211):
        print("Woda wrze")
    return F

#print(stanwody(x))

def CnaF(x):
    F= 32+32+x*1.8
    return F
def FnaC(x):
    C = (x-32)/1.8
    return C
def CnaK(x):
    K = x +237.15
    return K
def KnaC(x):
    C = x-273.15
    return C
def KnaF(x):
    F = x-273.15
    F = 32 + F *1.8
    return F
def FnaK(x):
    K = (x-32)/1.8
    K = K+2
    return K
def CnaD(x):
    D = (100-x)*1.33
    return D

#print(CnaD(50))