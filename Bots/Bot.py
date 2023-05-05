from abc import ABC, abstractmethod
from random import randint
from controle import Comando

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

    @abstractmethod
    def executa_comando(self, cmd):
        pass

    @abstractmethod
    def despedida(self):
        pass
