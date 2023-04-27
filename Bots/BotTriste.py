from Bots.Bot import Bot

class BotTriste(Bot):
    def __init__(self, nome):
        super().__init__(nome,{
            '1': ["Bom dia", "Só dia mesmo..."], 
            '2': ["Qual o seu nome?","Vex, mas tanto faz também, pode chamar do que cê quiser..."], 
            '3': ["Quero um conselho","Chore sempre que possível ︶︹︺"], 
            '4': ["Adeus","Mas já vai se despedir? ╥﹏╥"]
            })

    @property
    def nome(self):
        return super().nome
    
    @nome.setter
    def nome(self, nome):
        super().nome = nome

    def apresentacao(self):
        return f"Não gosto de apresentações, elas me deixam com vergonha..."

    def boas_vindas(self):
        return "Que bom que alguém apareceu por aqui..."

    def despedida(self):
        return "Novamente só..."
