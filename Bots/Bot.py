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
        for comando in self.comandos:
            comandos.append(f'{comando.id} - {comando.mensagem}')
        return comandos
        
    def executa_comando(self, cmd):
        comandos = dict()
        for comando in self.comandos:
            chave = comando.id
            mensagem = comando.getRandomResposta()
            comandos[chave] = mensagem
        if cmd in comandos.keys():
            return comandos[cmd]

    @abstractmethod
    def apresentacao():
        pass

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass