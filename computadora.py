from monitor import Monitor
from teclado import Teclado
from raton import Raton

class Computadora:
    
    contador_computadoras = 0
    
    def __init__(self, nombre, monitor, teclado, raton):
        # contador
        Computadora.contador_computadoras += 1
        self.__id_computadora = Computadora.contador_computadoras
        # propiedades
        self.__nombre = nombre
        self.__monitor = monitor
        self.__teclado = teclado
        self.__raton = raton

    def __str__(self):
        return (
            f"""
            {self.__nombre}: {self.__id_computadora} 
                Monitor: {self.__monitor}
                Teclado: {self.__teclado} 
                Ratón: {self.__raton}
                """
        )

# m = Monitor("LG", 24)
# t = Teclado("Red Dragon",'USB')
# r = Raton("Eagle Warrior",'USB')
    
# c = Computadora("Dell",m,t,r)
# print(c)

    
    
    
    
        
    