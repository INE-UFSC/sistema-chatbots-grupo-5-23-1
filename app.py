#encoding: utf-8
from Bots.BotFeliz import BotFeliz
from Bots.BotTriste import BotTriste
from Bots.BotZangado import BotZangado
from SistemaChatBot import SistemaChatBot as scb


###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"), BotFeliz("Feliz"), BotTriste("Vex")]

sys = scb.SistemaChatBot("CrazyBots", lista_bots)
sys.inicio()
