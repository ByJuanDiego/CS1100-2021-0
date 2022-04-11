Libreria de math:

    import math
    >>> print(math.pi)                  # imprime el valor aproximado de pi
    >>> print(round(math.pi, 4))        # imprime el valor de pi redondeado a 4 decimales
    >>> print(math.ceil(5/2))           # imprime el redondeo al siguiente entero de 2.5
    >>> print(math.floor(5/2))          # imprime el redondel al anterior entero de 2.5
    3.141592653589793
    3.1416
    3
    2

Libreria random:

    import random
    >>> print(random.random())          # imprime un float aleatorio entre 0.0 y 1.0 incluyendo el 0.0 pero no el 1.0
    >>> print(random.randint(1, 10))    # imprime un int aleatorio entre 1 y 10 contando ambos extremos
    >>> print(random.choice([1, 2, 3])) # imprime un elemento aleatorio de la lista
    >>> print(random.choice("abc"))     # imprime un caracter aleatorio del string
    0.5215391716079362
    6
    3
    a

Libreria time:

    import time
    >>> hora_local = time.localtime()
    >>> result = time.strftime("%I:%M:%S %p", hora_local)
    >>> print(result)
    11:08:56 PM

    >>> import time
    >>> segundos = 10
    >>> while True:
    >>>     print("{}".format(segundos))
    >>>     segundos -= 1
    >>>     time.sleep(1)
    >>>     if segundos == 0:
    >>>         break
    10
    9
    8
    7
    6
    5
    4
    3
    2
    1

Libreria json:

    import json

    dict = {'si': 'no'}
    with open("data.txt", "w") as file:
        json.dump(dict, file)

    json_str = json.dumps(dict, indent=4) # para que tenga formato de json
    print(json_str)
