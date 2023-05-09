#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotFeliz import BotFeliz
from Bots.BotTriste import BotTriste
from Bots.BotGPT import BotGPT

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"), BotFeliz("Joao Sorridente"), BotTriste("Tristinho"), BotGPT("Felipe")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
