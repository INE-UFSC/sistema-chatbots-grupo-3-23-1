from abc import ABC, abstractmethod
from random import randint
from Bots.comando import Comando

class Bot(ABC):
    def __init__(self, nome):
        self.__nome = nome
        self._comandos = [] # será que seria melhor transformar em um dicionário? pq assim, o comando precisa ser nevessariamente um número, mas se algum grupo 
        #criar um bot com um dicionário em que o comando não é um número, não vai rodar

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def mostra_comandos(self):
        cmds = [] 
        for comando in self._comandos:
            cmds.append(f'{comando.cmd}: {comando.pergunta}')
        return '\n'.join(cmds) ### o que é .join??

    @abstractmethod
    def apresentacao(self):
        pass

    @abstractmethod
    def boas_vindas(self):
        pass

    def executa_comando(self, cmd):
        cmd = int(cmd)
        if cmd in list(range(len(self._comandos) + 1)):
            return f' Você perguntou: {self._comandos[cmd-1].pergunta}\n-- Eu te respondo: {self._comandos[cmd-1].resposta}'
        else:
            return None

    @abstractmethod
    def despedida(self):
        pass
