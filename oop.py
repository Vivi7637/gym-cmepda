#posso importare la classe nel file come se fosse un modulo, e poi usarla come se fosse un modulo, ma non posso importare il file
import numpy as np

#self è l'instanza della classe, e viene passato automaticamente come primo argomento a tutti i metodi della classe, quindi non devo passarlo io, ma posso usarlo per accedere agli attributi dell'istanza

class Vector2d:

    SQRT2 = np.sqrt(2) #class attribute, it is shared by all instances of the class, and it can be accessed with the class name or with the instance name

    def __init__(self,x: float ,y: float): #costructor, it is called when an instance of the class is created, and it initializes the attributes
        self.x = float(x)          #every class has a special method called __init__ that is called when an instance of the class is created, and it initializes the attributes of the instance
        self.y = float(y)

    def  norm(self):
        return np.sqrt(self.x**2 + self.y**2)

    def dot(self,other:"Vector2d"):
        return self.x * other.x + self.y * other.y

    def __str__(self):
        return f"{self.__class__.__name__}({self.x},{self.y})"


if __name__ == "__main__": #main special variable, every module has a name,
    v = Vector2d(1.,1.)
    print (v)
    print(v.x,v.y)
    print (v.norm())
    print(v.dot(Vector2d(2.,2.)))


#methods are function connected to a class, and they are called with the instance of the class as first argument,
#so they can access the attributes of the instance ==> def "" are methods
#                                                  ==> members are attributes of the class, and they can be data members or methods
#rom oop import Vector2d

#encapsulation
#The state of an object should only be accessed and altered through its publicly exposed interface