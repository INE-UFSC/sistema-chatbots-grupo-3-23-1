class Comando():
    def __init__(self, cmd, pergunta, resposta):
        self.__cmd = cmd
        self.__pergunta = pergunta
        self.__resposta = resposta
    
    @property
    def cmd(self):
        return self.__cmd
    
    @property
    def pergunta(self):
        return self.__pergunta
    
    @property
    def resposta(self):
        return self.__resposta