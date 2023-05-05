from abc import ABCMeta, abstractmethod

class MontyPython(metaclass=ABCMeta):
    @abstractmethod
    def joke(self):
        pass
    
    @abstractmethod
    def punchline(self):
        pass

class ArgumentClinic(MontyPython):
    def joke(self):
        return "Hahahahahah"
    
#Obtenemos un typeerror, lo solucionamos:

class ArgumentClinic(MontyPython):
    def joke(self):
        return "Hahahahahah"
    
    def punchline(self):
        return "Send in the constable!"
    

pop=ArgumentClinic()
print(pop.punchline())
print(pop.joke())
