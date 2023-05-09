from Bots.Bot import Bot
from Comando.Comando import Comando

class BotFeliz(Bot):
    def __init__(self, nome):
        super().__init__(nome,[
            Comando('1', "Bom dia", "Bom dia para você também, ótimo dia aliás!!!"),
            Comando('2', "Qual o seu nome?", f"Olá, me chamo {nome}!!!"),
            Comando('3', "Quero um conselho", "Seja feliz e viva a vida alegramente! :)"),
            Comando('4', "Adeus", "Poxa, já está indo? Até uma próxima vez caro amigo!")
            ])

    @property
    def nome(self):
        return super().nome

    @nome.setter
    def nome(self, nome):
        super().nome = nome

    def apresentacao(self):
        return f"Olá meu nome é {super().nome} e estou aqui para te ajudar!!!"
    
    def boas_vindas(self):
        return f"Muito prazer em ser ecolhido por você, meu nome é {super().nome} e me alegra ter sua presença aqui!"

    def despedida(self):
        return "Espero ter sido útil para você, me  escolha mais vezes para podermos conversar por mais tempo!"
