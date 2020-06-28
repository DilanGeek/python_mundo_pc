class Monitor:
    
    contador_monitores = 0
    
    def __init__(self, marca, tamanio):
        Monitor.contador_monitores += 1
        self.__id_monitor = Monitor.contador_monitores
        self.__marca = marca
        self.__tamanio = tamanio
    
    def __str__(self):
        return (
            f"id: {self.__id_monitor},"
            f"marca: {self.__marca},"
            f"tamanio: {self.__tamanio},"
        )    