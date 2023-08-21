def intChecker(texto):
    while True:
        try:
            numero = int(input(texto))
            break
        except ValueError:
            print("Ingrese un número entero\n")
    return numero


logo1 = """
 _   _       _       _ 
| | | |     | |     | |
| |_| | ___ | | __ _| |
|  _  |/ _ \| |/ _` | |
| | | | (_) | | (_| |_|
\_| |_/\___/|_|\__,_(_)
                       
                       
"""


logo2 = """
______            _ 
| ___ \          | |
| |_/ /_   _  ___| |
| ___ \ | | |/ _ \ |
| |_/ / |_| |  __/_|
\____/ \__, |\___(_)
        __/ |       
       |___/        
"""