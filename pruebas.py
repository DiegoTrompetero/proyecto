import random
class Flota ():
    def __init__(self,posiones): 
        self.posiones= posiones

class Buque3(Flota):
    def __init__ (self,posiones,tipo):
        Flota.__init__(self,posiones)
        self.tipo = tipo

    def catalogar (self):
        print ("Un buque de {} posiones {} pista de aterrizaje".format(self.posiones,self.tipo))

class Buque2(Flota):
    def __init__ (self,posiones,tipo):
        Flota.__init__(self,posiones)
        self.tipo = tipo

    def catalogar (self):
        print ("Un buque de {} posiones {} la capacidad de comunicarse".format(self.posiones,self.tipo))

class Submarinos (Flota):
    def __init__ (self,posiones,tipo):
        Flota.__init__(self,posiones)
        self.tipo = tipo

    def catalogar (self):
        print ("Un Submarino de {} posion {} ".format(self.posiones,self.tipo))


print("El enemigo tiene lo siguiente en el tablero:")
Buquetres = Buque3("tres", random.choice(["con", "sin"])).catalogar()
Buquedos =Buque2("dos", random.choice(["con", "sin"])).catalogar()
sub1 = Submarinos("una", random.choice (["sumergido", "sin sumergirse"])).catalogar() 
sub2 = Submarinos("una", random.choice (["sumergido", "sin sumergirse"])).catalogar()
sub3 = Submarinos("una", random.choice (["sumergido", "sin sumergirse"])).catalogar()
sub4= Submarinos("una", random.choice (["sumergido", "sin sumergirse"])).catalogar()


