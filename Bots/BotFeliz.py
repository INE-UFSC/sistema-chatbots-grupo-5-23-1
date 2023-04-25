from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self, nome):
        self.__nome = nome
        super().__comandos = {
            1: ["Bom dia", "Ótimo dia!!!"],
            2: ["Qual o seu nome?", f"Olá, me chamo {self.__nome} e estou aqui para te ajudar!"],
            3: ["Quero um conselho", "Seja feliz e viva a vida alegramente! :)"],
            4: ["Adeus", "Poxa! Já está indo? Que pena..."]
            }

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return f"Aaaargh. Meu nome é {self.__nome} e eu te odeio!(Mais que o Yoda)"
    
    def boas_vindas(self):
        boas_vindas = "Tanto bot pra ser escolhido e tu me escolhe???"
        print(boas_vindas)

    def despedida(self):
        despedida = "Graças a Deus!"
        print(despedida)

    def mostra_comandos(self):
        pass
    
    def executa_comando(self,cmd):
        pass