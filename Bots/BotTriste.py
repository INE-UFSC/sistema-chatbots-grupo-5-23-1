from Bots.Bot import Bot

class BotTriste(Bot):
    def __init__(self, nome):
        self.__nome = nome
        super().__comandos = {
            1: ['Só dia mesmo...'], 
            2: ['Pode chamar do que cê quiser'], 
            3: ['Chore sempre que possível'], 
            4: ['Mas já vai se despedir? :(']
            }

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao_triste(self):
        pass

    def executa_comando_triste(self, cmd):
        print(self.__cmd[1])
        print(self.__cmd[2])
        print(self.__cmd[3])
        print(self.__cmd[4])

    def boas_vindas_triste(self):
        boas_vindas = "Que bom que alguém apareceu por aqui..."
        print(boas_vindas)

    def despedida_triste(self):
        despedida = "Novamente sozinho..."
        print(despedida)
 
    def mostra_comandos_triste(self, cmd):
        pass