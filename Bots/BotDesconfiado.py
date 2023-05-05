

import json
from Bots.Bot import Bot
from Comando.Comando import Comando

class BotDesconfiado(Bot):
    def __init__(self, nome: str, comandos: Comando, urlJSON: str):
        self.__nome = nome
        self.__urlJSON = urlJSON
        self.__comandos = comandos

    @property
    def nome(self):
        return super().nome
    
    @nome.setter
    def nome(self, nome):
        super().nome = nome

    def apresentacao(self):
        return f"Nunca fiz nada de errado, então, não tem o porque me escolher. Mas se quiser, sem problemas!"

    def boas_vindas(self):
        return "Adorei que me escolheu!"

    def despedida(self):
        return "Ufa essa foi por pouco...Quer dizer...Bye!s"

    def mostra_comandos(self):
        for comando in self.__comandos:
            return self.__comandos(comando)

    def cria_comandos(self, comando_novo):
        novo_comandos = self.__comandos.json.dumps(comando_novo)
        return novo_comandos