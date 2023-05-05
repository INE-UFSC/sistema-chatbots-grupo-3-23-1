from abc import ABC, abstractmethod
from random import randint
from Bots.comando import Comando

class Bot(ABC):
    def __init__(self, nome):
        self.__nome = nome
        self._comandos = [Comando]

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
        return '\n'.join(cmds)

    @abstractmethod
    def apresentacao(self):
        pass

    @abstractmethod
    def boas_vindas(self):
        pass

    def executa_comando(self, cmd):
        cmd = int(cmd)
        return f' Você perguntou: {self._comandos[cmd-1].pergunta}\n-- Eu te respondo: {self._comandos[cmd-1].resposta}'

    @abstractmethod
    def despedida(self):
        pass
