#encoding: utf-8
from Bots.BotFeliz import BotFeliz
from Bots.BotTriste import BotTriste
from Bots.BotZangado import BotZangado
from SistemaChatBot import SistemaChatBot as scb
from BotsExternos.BotFelizGrupo3 import BotFelizGrupo3

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"), BotTriste("Vex"), BotFeliz("Feliz")]#, BotFelizGrupo3("Rita")]

sys = scb.SistemaChatBot("CrazyBots", lista_bots)
sys.inicio()
