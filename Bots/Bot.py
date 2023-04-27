from abc import ABC, abstractmethod

class Bot(ABC):

    def __init__(self, nome, comandos):
        self.__nome = nome
        self.__comandos = comandos

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
        comandos = list()
        for chave, valor in self.__comandos.items():
            comandos.append(f'{chave} - {valor[0]}')
        return comandos
        
    def executa_comando(self, cmd):
        if cmd in self.__comandos.keys():
            return self.__comandos[cmd][1]

    @abstractmethod
    def apresentacao():
        pass

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass