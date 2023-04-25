##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(self, nome, comandos):
        self.__nome = nome
        self.__comandos = {}

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def comandos(self):
        return self.__comandos
    
    @comandos.setter
    def comandos(self, comandos):
        self.__comandos = comandos

    def mostra_comandos(self):
        for chave, valor in self.__comandos.items():
            print(f'{chave} - {valor[0]}')
        
    def executa_comando(self,cmd):
        print(self.__comandos[cmd][1])

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass