def my_sum(x, y):
    """A function that sums. """
    return x+y


def my_mul(x, y):
    """A function that multiply. """
    return x*y

def palabras(cadena):
    diccionario = dict()
    palabras = cadena.split(" ")
    for i in palabras:
        if i in diccionario.keys():
            diccionario[i] = diccionario[i]+1
        else:
                diccionario[i] = 1
    return diccionario
