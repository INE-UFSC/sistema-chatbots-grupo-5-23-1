import random


class Comando():
    # recebe o id (inteiro), a mensagem e as respostas (opcional)
    def __init__(self, id, mensagem, respostas = []):
        self.__id = id
        self.__mensagem = mensagem
        self.__respostas = respostas

    @property
    def id(self):
        return self.__id

    @property
    def mensagem(self):
        return self.__mensagem 

    # retorna uma resposta aleatória
    def getRandomResposta(self):
        resposta_aleatoria = random.choice(self.__respostas)
    
    # adiciona resposta
    def addResposta(self, resposta):
        if resposta not in self.__respostas:
            self.__respostas.append(resposta)
        else:
            print('Resposta já existente!')

    # remove resposta (opcional)
    def delResposta(self, resposta):
        if resposta in self.__respostas:
            self.__respostas.pop(resposta)
        else:
            print('Resposta não existente!')